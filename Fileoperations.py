import os

import requests
from bs4 import BeautifulSoup

re = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
r_html = re.text

soup = BeautifulSoup(r_html, "html.parser")

# print(soup.prettify())
filename1 = input("Enter file name:")
# sou=soup.body.find_all("section",{"class":"content-section"})
print(os.getcwd() + '/' + ''.join(filename1) + ".txt")
with open(os.getcwd() + '/' + ''.join(filename1) + ".txt", 'w') as fp:
    for con in soup.find_all("section", {"class": "content-section"}):
        fp.write(con.text)
        fp.write("\n")
