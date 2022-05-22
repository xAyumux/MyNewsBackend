import requests
from bs4 import BeautifulSoup
import re


def yahoo():
    load_url = "https://news.yahoo.co.jp/ranking/access/news"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    count = 1

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

        articleDict = {"rank": rank, "title": title, "url": url}
        articlesDict[count] = articleDict

        count += 1

    return articlesDict


def gizmodo():
    url = "https://www.gizmodo.jp/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    count = 1

    articlesDict = {}

    elems = soup.find_all(href=re.compile("https://www.gizmodo.jp/2022/05"))
    for elem in elems:
        title = elem.contents[0].text
        url = elem.attrs['href']

        articleDict = {"title": title, "url": url}
        articlesDict[count] = articleDict

        count += 1

    return articlesDict
