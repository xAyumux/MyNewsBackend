import requests
from bs4 import BeautifulSoup
import re
 
url = "https://www.yahoo.co.jp/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
 
elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
for elem in elems:
    print(elem.contents[0].text)
    print(elem.attrs['href'])