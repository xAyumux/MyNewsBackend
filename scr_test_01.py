import requests
from bs4 import BeautifulSoup
import re
 
url = "https://www.yahoo.co.jp/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
 
elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

pickup_links = [elem.attrs['href'] for elem in elems]

#一覧のリンクを順に処理
for pickup_link in pickup_links:
    #Pickupページへ遷移しページの情報を取得
    pickup_res = requests.get(pickup_link)
    pickup_soup = BeautifulSoup(pickup_res.text, "html.parser")
    
    #ニュースページへのリンクを取得
    pickup_elem = pickup_soup.find("p", class_="sc-bYzVrU umXBl")    
    news_link = pickup_elem.contents[0].attrs['href']
 
    #ニュースページの情報を取得
    news_res = requests.get(news_link)
    news_soup = BeautifulSoup(news_res.text, "html.parser")

    #タイトルとURLを表示
    print(news_soup.title.text)
    print(news_link)
    
    #ニュースのサムネイル&テキスト情報を取得し表示
    img_res = pickup_soup.find(type="image/jpeg")
    news_img = img_res.attrs['srcset']
    print(news_img)
    detail_text = news_soup.find(class_=re.compile("highLightSearchTarget"))
    print(detail_text.text if hasattr(detail_text, "text") else '',end='\n\n\n\n')