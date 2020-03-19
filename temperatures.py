from bs4 import BeautifulSoup
import requests

url='https://www.currentresults.com/Yearly-Weather/Canada/QC/Montreal/extreme-annual-montreal-low-temperature.php'

page = requests.get(url)
# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='maincol')
job_elems = results.find_all('table', class_='articletable')
for job_elem in job_elems:
    print(job_elem, end='\n'*2)
