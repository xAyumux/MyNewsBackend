import requests
from bs4 import BeautifulSoup
import re
 
url = "https://www.gizmodo.jp/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
 
elems = soup.find_all(href=re.compile("https://www.gizmodo.jp/2022/05"))
for elem in elems:
    print("�^�C�g�� : "+elem.contents[0].text)
    print("�����N�� : "+elem.attrs['href'])
    print( )