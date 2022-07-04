from urllib import response
import requests
import pprint
from bs4 import BeautifulSoup
from soupsieve import select
from transliterate import translit, get_available_language_codes

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
text_translite=translit(input('write name of vacancy here:').replace(' ', '_'), 'ru', reversed=True)
url = f'https://hh.ru/vacancies/{text_translite}'.replace("'", "").lower()
print(url)
session = requests.Session()
response = session.get(url, headers=headers)
dom = BeautifulSoup(response.text, 'html.parser')
vacancies = dom.select('span.g-user-content')
print(vacancies)

