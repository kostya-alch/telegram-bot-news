import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def get_first_news():
   headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
   }

   url = "https://www.securitylab.ru/news/"
   r = requests.get(url=url, headers=headers)

   soup = BeautifulSoup(r.text, "lxml")
   articles_cards = soup.find_all("a", class_="article-card")

   for article in articles_cards:
      article_title = article.find("h2", class_="article-card-title").text.strip()
      article_desc = article.find("p").text.strip()
      article_url= f'https://www.securitylab.ru/news/{article.get("href")}'

      article_date_time = article.find("time").get("datetime")
      date_from_iso = datetime.fromisoformat(article_date_time)
      date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
      article_date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").timetuple())

      print(f"{article_title} | {article_url} | {article_date_timestamp}")

get_first_news()
