from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup
# import pandas as pd

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


@app.get("/hello")
def Hello():
    return {"Hello": "World!"}


# @app.get("/articles/{site_name}")
# def GetArticle():
#     pass


@app.get("/articles/yahoonews")
def GetYahoo():
    load_url = "https://news.yahoo.co.jp/ranking/access/news"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    # columns = ["Rank", "Article_Name", "Url"]
    # df = pd.DataFrame(columns=columns)
    # print(df)

    count = 0

    articlesDict = {}

    topic = soup.find(class_="newsFeed_list")
    for element in topic.find_all("a"):
        if(count < 9):
            rank = element.text[0:1]
            title = element.text[1:]
        else:
            rank = element.text[0:2]
            title = element.text[2:]
        # print(rank)
        # print(title)
        articlesDict[rank] = title

        # url = element.get("href")
        # print(url)

        # row = pd.Series([rank, title, url], columns)
        # df = df.append(row, columns)
        count += 1

    return articlesDict
