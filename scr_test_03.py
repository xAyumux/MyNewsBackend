import requests
from bs4 import BeautifulSoup
import re

url = "https://www.itmedia.co.jp/"
res = requests.get(url)

elems = soup.find_all(class_ = "colBoxTitle")
for elem in elems:
    print("�^�C�g�� : "+elem.contents[0].text)
    elem1 = elem.find("a")
    print("�����N�� : "+elem1.attrs['href'])