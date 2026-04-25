#1. Accessing the website through URL
import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)

print(response.status_code)
#2. Web Scraping
#Printing Quotes
soup=BeautifulSoup(response.text,"html.parser")
quotes=soup.find_all("span",class_="text")
for quote in quotes:
    print(quote.text)
#Printing Authors
data=soup.find_all("div",class_="quote")
for item in data:
    quote=item.find("span",class_="text").text
    author=item.find("small",class_="author").text

    print(quote,"-",author)

#4. Stroring data in dataframe
import pandas as pd

quotes_list=[]
authors_list=[]

for item in data:
    quotes_list.append(item.find("span",class_="text").text)
    authors_list.append(item.find("small",class_="author").text)

df=pd.DataFrame({
    "Quotes":quotes_list,
    "Authors":authors_list
})

df
#5. Save to Excel
df.to_excel("quotes.xlsx", index=False)