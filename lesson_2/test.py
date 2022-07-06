from cgitb import text
import requests
import pprint
from bs4 import BeautifulSoup
from soupsieve import select
from transliterate import translit, get_available_language_codes

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
text_translite=translit(input('write name of vacancy here:').replace(' ', '_').replace("'", "").lower(), 'ru', reversed=True)
url = 'https://hh.ru/vacancy'
params = {'text': text_translite}
session = requests.Session()
resp = session.get(url, headers=headers, params=params)
print(resp)
dom = BeautifulSoup(resp.content, 'html.parser')
#vacancy = dom.find('vacancy-serp-item')
#print(vacancy)
