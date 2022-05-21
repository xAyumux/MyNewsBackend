{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fdc4d15a-beb2-4ff1-a910-260718e15c55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "タイトル：中国新たなガス田か 首相「遺憾」NEW\n",
      "リンク先：https://news.yahoo.co.jp/pickup/6427121\n",
      "タイトル：国後島で発見の遺体 不明甲板員か\n",
      "リンク先：https://news.yahoo.co.jp/pickup/6427118\n",
      "タイトル：発熱者急増の北朝鮮 実態は不透明NEW\n",
      "リンク先：https://news.yahoo.co.jp/pickup/6427116\n",
      "タイトル：どう暮らせば 物価高が困窮に拍車NEW\n",
      "リンク先：https://news.yahoo.co.jp/pickup/6427120\n",
      "タイトル：スカイツリー10周年 東武支える柱\n",
      "リンク先：https://news.yahoo.co.jp/pickup/6427109\n",
      "タイトル：レア?大谷が映像でハット&ひげ姿NEW\n",
      "リンク先：https://news.yahoo.co.jp/pickup/6427122\n",
      "タイトル：本田翼 理不尽はある程度仕方ない\n",
      "リンク先：https://news.yahoo.co.jp/pickup/6427113\n",
      "タイトル：タレントの紗綾 結婚と妊娠を発表\n",
      "リンク先：https://news.yahoo.co.jp/pickup/6427117\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import re\n",
    " \n",
    "url = \"https://www.yahoo.co.jp/\"\n",
    "res = requests.get(url)\n",
    "soup = BeautifulSoup(res.text, \"html.parser\")\n",
    "\n",
    "elems = soup.find_all(href=re.compile(\"news.yahoo.co.jp/pickup\"))\n",
    "\n",
    "pickup_links = [elem.attrs['href'] for elem in elems]\n",
    "for elem in elems:\n",
    "    print(\"タイトル：\"+elem.contents[0].text)\n",
    "    print(\"リンク先：\"+elem.attrs['href'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e3475bf-27dc-4cf9-a1c3-be1374b178b9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
