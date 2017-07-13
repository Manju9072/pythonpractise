import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.thehindu.com/")
r_html = res.text

sop = BeautifulSoup(r_html, 'html.parser')

for el in sop.find_all('div', class_="story-card"):
    try:
        print(el.a)
    except Exception as e:
        pass
