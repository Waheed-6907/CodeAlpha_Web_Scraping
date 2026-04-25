#1. Accessing URL
import requests
from bs4 import BeautifulSoup

url="https://realpython.github.io/fake-jobs/"
response=requests.get(url)
print(response.status_code)
#2. Web Scraping
soup=BeautifulSoup(response.text,"html.parser")
jobs=soup.find_all("div",class_="card-content")
#3. Printing all jobs
for job in jobs:
    title=job.find("h2",class_="title").text.strip()
    company=job.find("h3",class_="company").text.strip()
    location=job.find("p",class_="location").text.strip()

    print(title,"-",company,"-",location)

#4. Converting into table
import pandas as pd

titles_list=[]
company_list=[]
location_list=[]

for job in jobs:
    titles_list.append(job.find("h2",class_="title").text.strip())
    company_list.append(job.find("h3",class_="company").text.strip())
    location_list.append(job.find("p",class_="location").text.strip())
   
print(f"Total jobs scraped: {len(jobs)}")

df=pd.DataFrame({
    "JOB TITLE":titles_list,
    "COMPANY":company_list,
    "LOCATION":location_list
})

df
#5. Save to Excel
df.to_excel("fake_jobs.xlsx", index=False)

#6. Filtering Data
#Location wise
print("JOBS IN LOCATION 'AA':")
aa_jobs=df[df["LOCATION"].str.contains("AA")]
print(aa_jobs)

print("JOBS IN LOCATION 'AE':")
ae_jobs=df[df["LOCATION"].str.contains("AE")]
print(ae_jobs)

#Domain wise
print("PYTHON JOBS:")
python_jobs=df[df["JOB TITLE"].str.contains("Python")]
print(python_jobs)

print("TEACHING JOBS:")
teaching_jobs=df[df["JOB TITLE"].str.contains("Teacher")]
print(teaching_jobs)
#Statistics
print(df["LOCATION"].value_counts())

top_location = df["LOCATION"].value_counts().idxmax()
print("Most jobs in:", top_location)