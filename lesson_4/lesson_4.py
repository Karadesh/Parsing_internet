from lxml import html
import requests
from pprint import pprint

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
url = 'https://yandex.ru/news/'

session = requests.Session()
response = session.get(url, headers=header)
dom = html.fromstring(response.text)
items = dom.xpath("//div[contains(@class,'mg-grid__col')]")
for item in items:
    news = {}
    title = item.xpath(".//h2[@class='mg-card__title']//text()")
    print(title)
#    text =
#    link =