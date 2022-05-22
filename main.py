from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup
import re
from pydantic import BaseModel
import scraping

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Keywords(BaseModel):
    keywords: List


@app.get("/hello")
def hello():
    return {"Hello": "World!"}


@app.get("/articles/yahoonews")
def get_yahoo():
    articlesDict = scraping.yahoo()
    return articlesDict


@app.get("/articles/gizmodo")
def get_gizmodo():
    articlesDict = scraping.gizmodo()
    return articlesDict


@app.post("/articles/keywords")
def search_keywords(keywords: Keywords):
    # yahoo
    load_url = "https://news.yahoo.co.jp/ranking/access/news"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    count = 1
    articleNumber = 1

    articlesDict = {}

    topic = soup.find(class_="newsFeed_list")
    for element in topic.find_all("a"):
        if(count < 9):
            rank = element.text[0:1]
            title = element.text[1:]
        else:
            rank = element.text[0:2]
            title = element.text[2:]

        url = element.get("href")

        for keyword in keywords.keywords:
            if keyword in title:
                articleDict = {"rank": rank, "title": title, "url": url}
                articlesDict[articleNumber] = articleDict
                articleNumber += 1

        count += 1

    # gizmodo
    url = "https://www.gizmodo.jp/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    elems = soup.find_all(href=re.compile("https://www.gizmodo.jp/2022/05"))
    for elem in elems:
        title = elem.contents[0].text
        url = elem.attrs['href']

        for keyword in keywords.keywords:
            if keyword in title:
                articleDict = {"title": title, "url": url}
                articlesDict[articleNumber] = articleDict
                articleNumber += 1

        count += 1

    return articlesDict
