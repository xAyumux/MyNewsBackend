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

#�ꗗ�̃����N�����ɏ���
for topic_link in topic_links:
    
    #�����L���O���L�^
    for i in range(0,40):
        Rank = i
        Rank += 1
        print(Rank)
        
        #topic�y�[�W�֑J�ڂ��y�[�W�̏����擾
        topic_res = requests.get(topic_link)
        topic_soup = BeautifulSoup(topic_res.text, "html.parser")
        
        #�j���[�X�y�[�W�ւ̃����N���擾
        topic_elem = topic_soup.find("meta", content=re.compile("news.yahoo.co.jp/articles"))
        news_link = topic_elem.attrs["content"]
        
        #�j���[�X�y�[�W�̏����擾
        news_res = requests.get(news_link)
        news_soup = BeautifulSoup(news_res.text, "html.parser")
        
        #�^�C�g����URL��\��
        Article_Name = topic_soup.title.text
        print(Article_Name)
        Url = news_link
        print(Url)
        
        #�j���[�X�̃T���l�C��&�e�L�X�g�����擾���\��
        img_res = news_soup.find(type="image/jpeg")
        Thumnail = img_res.attrs['srcset']
        print(Thumnail)
        Text = news_soup.find(class_=re.compile("highLightSearchTarget"))
        print(Text.text if hasattr(Text, "text") else '',end='\n\n\n\n')