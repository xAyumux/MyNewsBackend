import requests
from bs4 import BeautifulSoup
import re


def yahoo_news():
    load_url = "https://www.yahoo.co.jp/"
    res = requests.get(load_url)
    soup = BeautifulSoup(res.text, "html.parser")

    elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

    pickup_links = [elem.attrs['href'] for elem in elems]

    count = 1

    articles_dict = {}

    # 一覧のリンクを順に処理
    for pickup_link in pickup_links:
        # Pickupページへ遷移しページの情報を取得
        pickup_res = requests.get(pickup_link)
        pickup_soup = BeautifulSoup(pickup_res.text, "html.parser")

        # ニュースページへのリンクを取得
        pickup_elem = pickup_soup.find("p", class_="sc-bYzVrU umXBl")
        news_link = pickup_elem.contents[0].attrs['href']

        # ニュースページの情報を取得
        news_res = requests.get(news_link)
        news_soup = BeautifulSoup(news_res.text, "html.parser")

        # タイトルとURLを表示
        title = news_soup.title.text
        url = news_link
        print(news_soup.title.text)
        print(news_link)

        # ニュースのサムネイル&テキスト情報を取得し表示
        img_res = pickup_soup.find(type="image/jpeg")
        img_url = img_res.attrs['srcset']
        print(img_url)
        detail_text = news_soup.find(
            class_=re.compile("highLightSearchTarget"))
        print(detail_text.text if hasattr(
            detail_text, "text") else '', end='\n\n\n\n')
        snippet = detail_text.text

        article_dict = {"title": title, "url": url,
                        "img_url": img_url, "snippet": snippet}
        articles_dict[count] = article_dict

        count += 1

    return articles_dict


def yahoo_ranking():
    load_url = "https://news.yahoo.co.jp/ranking/access/news"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    elems = soup.find_all(href=re.compile("news.yahoo.co.jp/article"))

    topic = soup.find_all(href=re.compile("news.yahoo.co.jp/articles"))
    topic_links = [elem.attrs['href'] for elem in elems]

    count = 1

    articles_dict = {}

    # 一覧のリンクを順に処理
    for topic_link in topic_links:

        # ランキングを記録
        for i in range(0, 40):
            Rank = i
            Rank += 1
            rank = Rank

            # topicページへ遷移しページの情報を取得
            topic_res = requests.get(topic_link)
            topic_soup = BeautifulSoup(topic_res.text, "html.parser")

            # ニュースページへのリンクを取得
            topic_elem = topic_soup.find(
                "meta", content=re.compile("news.yahoo.co.jp/articles"))
            news_link = topic_elem.attrs["content"]

            # ニュースページの情報を取得
            news_res = requests.get(news_link)
            news_soup = BeautifulSoup(news_res.text, "html.parser")

            # タイトルとURLを表示
            title = topic_soup.title.text
            url = news_link

            # ニュースのサムネイル&テキスト情報を取得し表示
            img_res = news_soup.find(type="image/jpeg")
            img_url = img_res.attrs['srcset']
            Text = news_soup.find(class_=re.compile("highLightSearchTarget"))
            snippet = Text.text

            article_dict = {"rank": rank, "title": title,
                            "url": url, "img_url": img_url, "snippet": snippet}
            articles_dict[count] = article_dict

            count += 1

    return articles_dict


def gizmodo():
    load_url = "https://www.gizmodo.jp/"
    res = requests.get(load_url)
    soup = BeautifulSoup(res.text, "html.parser")

    count = 1

    articles_dict = {}

    elems = soup.find_all(href=re.compile("https://www.gizmodo.jp/2022/05"))
    for elem in elems:
        title = elem.contents[0].text
        url = elem.attrs['href']

        article_dict = {"title": title, "url": url}
        articles_dict[count] = article_dict

        count += 1

    return articles_dict


def itmedia():
    load_url = "https://www.itmedia.co.jp/"
    res = requests.get(load_url)
    soup = BeautifulSoup(res.text, "html.parser")

    count = 1

    articles_dict = {}

    elems = soup.find_all(class_="colBoxTitle")
    for elem in elems:
        title = elem.contents[0].text
        elem1 = elem.find("a")
        url = elem1.attrs['href']

        article_dict = {"title": title, "url": url}
        articles_dict[count] = article_dict

        count += 1

    return articles_dict
