import requests
from bs4 import BeautifulSoup
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
response = requests.get('https://attack.mitre.org/groups/',headers=headers)

soup = BeautifulSoup(response.text,'html.parser')
table = soup.find('table')
headers=[]
for i in table.find_all('tr'):    
    title=i.text.strip()    
    headers.append(title)
