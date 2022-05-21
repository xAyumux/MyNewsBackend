import requests
from bs4 import BeautifulSoup
import re

url = "https://www.itmedia.co.jp/"
res = requests.get(url)

elems = soup.find_all(class_ = "colBoxTitle")
for elem in elems:
    print("タイトル : "+elem.contents[0].text)
    elem1 = elem.find("a")
    print("リンク先 : "+elem1.attrs['href'])