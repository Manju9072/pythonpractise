import requests
from bs4 import BeautifulSoup

re = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
r_html = re.text

soup = BeautifulSoup(r_html, "html.parser")

# print(soup.prettify())

# sou=soup.body.find_all("section",{"class":"content-section"})

for con in soup.find_all("section", {"class": "content-section"}):
    print(con.text)
