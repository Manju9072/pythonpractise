import requests
from bs4 import BeautifulSoup

r = requests.get("http://timesofindia.indiatimes.com/")
r_html = r.text
# print(r_html)
soup = BeautifulSoup(r_html, 'html.parser')
t5 = []
for t2 in soup.body.div.find_all('ul'):

    if 'data-vr-zone' in t2.attrs:
        t5.append(t2.attrs['data-vr-zone'])
    else:
        pass

dic = {}
dic2 = {}
print(t5)
for story in t5:

    for te in soup.body.div.find_all('ul', attrs={'data-vr-zone': story}):

        try:

            news = te.stripped_strings

            hrf = te.find('a', href=True)
            for e in te.find_all('li'):
                if 'http://' not in e.find("a")['href']:
                    dic[e.text.replace('\n', "").strip()] = 'http://timesofindia.indiatimes.com/' + e.find("a")['href']
                else:
                    dic[e.text.replace('\n', "").strip()] = e.find("a")['href']
            dic2[story] = dic


        except Exception as e:
            pass

    print(
        "------------------------------------------------" + story + "-----------------------------------------------------")
    for key, values in dic.items():

        if 'background-image:url' in values or 'coldetect' in values or 'Ad' in values or '\n' in values:
            pass
        else:
            print(key)
            print(values)

    print(
        "--------------------------------------------------------------------------------------------------------------")
