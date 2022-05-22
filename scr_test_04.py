import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

load_url = "https://news.yahoo.co.jp/ranking/access/news"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
elems = soup.find_all(href=re.compile("news.yahoo.co.jp/article"))

topic = soup.find_all(href=re.compile("news.yahoo.co.jp/articles"))
topic_links = [elem.attrs['href'] for elem in elems]

#一覧のリンクを順に処理
for topic_link in topic_links:
    
    #ランキングを記録
    for i in range(0,40):
        Rank = i
        Rank += 1
        print(Rank)
        
        #topicページへ遷移しページの情報を取得
        topic_res = requests.get(topic_link)
        topic_soup = BeautifulSoup(topic_res.text, "html.parser")
        
        #ニュースページへのリンクを取得
        topic_elem = topic_soup.find("meta", content=re.compile("news.yahoo.co.jp/articles"))
        news_link = topic_elem.attrs["content"]
        
        #ニュースページの情報を取得
        news_res = requests.get(news_link)
        news_soup = BeautifulSoup(news_res.text, "html.parser")
        
        #タイトルとURLを表示
        Article_Name = topic_soup.title.text
        print(Article_Name)
        Url = news_link
        print(Url)
        
        #ニュースのサムネイル&テキスト情報を取得し表示
        img_res = news_soup.find(type="image/jpeg")
        Thumnail = img_res.attrs['srcset']
        print(Thumnail)
        Text = news_soup.find(class_=re.compile("highLightSearchTarget"))
        print(Text.text if hasattr(Text, "text") else '',end='\n\n\n\n')