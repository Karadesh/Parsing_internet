from lxml import html
import requests
from pprint import pprint
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.yanewsdb
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
url = 'https://yandex.ru/news/'

session = requests.Session()
response = session.get(url, headers=header)
dom = html.fromstring(response.text)
items = dom.xpath("//div[contains(@class,'mg-grid__col')]")
for item in items:
    news = {}
    title = item.xpath(".//h2[@class='mg-card__title']//text()")
    if title:
        title_text = title[0]
        title_text_corrected = title_text.replace('\xa0', '')
        news['title'] = title_text_corrected
    text = item.xpath(".//div[@class='mg-card__annotation']//text()")
    if text:
        text_text = text[0]
        text_text_corrected = text_text.replace('\xa0', '')
        news['text'] = text_text_corrected
    link = item.xpath(".//h2[@class='mg-card__title']//@href")
    if link:
        link_text = link[0]
        finder = db.yanewsdb.find({'link':{'$eq':link_text}})
        if finder!= link_text:
            news['link'] = link_text
    if news:        
        db.yanewsdb.update_one(news)


    