import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
source_code = requests.get(url)
plain_text = source_code.text

soup = BeautifulSoup(plain_text)
count = 0
for link in soup.findAll('a',href=re.compile("trump")):
    if count < 5:
        count = count + 1
       # print(count)
        x = link.get('href')
        print(x)

