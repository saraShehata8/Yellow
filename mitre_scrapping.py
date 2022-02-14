#Find the URL that you want to scrape.
#Inspecting the Page.
#Find the data you want to extract.
#Write the code.
#Run the code and extract the data.
#Store the data in the required format.
import requests
from bs4 import BeautifulSoup
 #when a web browser requests a web page from a web server, the web browser user-agent string is included in the HTTP request header
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
response = requests.get('https://attack.mitre.org/groups/',headers=headers)
#soup object search in html for the data you need
soup = BeautifulSoup(response.text,'html.parser')
table = soup.find('table')
headers=[]
for i in table.find_all('tr'):    
    title=i.text.strip()    
    headers.append(title)
print(headers)    
    
    
    
