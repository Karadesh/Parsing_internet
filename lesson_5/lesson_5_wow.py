from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pymongo
from pymongo.errors import DuplicateKeyError
from pymongo import MongoClient

#link to new db chromienews
client = MongoClient('mongodb://localhost:27017')
db = client.chromienews

s = Service('./geckodriver')
options = Options()
#options.add_argument('start-maximized')
driver = webdriver.Firefox(service=s)

driver.get('https://www.chromiecraft.com/en/news/')
#pushing cookie button to agree
cookie_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((
        By.CLASS_NAME, 'tibrr-cookie-consent-button'))
        )
try:
    cookie_button.click()
except:
    pass
#pusing 'All News' button
all_news = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'All News')))
all_news.click()
#clicking on 'Load More' n times to see all news
while True:
    try:
        load_more = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Load More')))
        load_more.click()
    except TimeoutException:
        break
news = driver.find_elements(By.CLASS_NAME, 'nk-post-content')
#find news elements and making dict
for i in news:
    news_dict = {}
    news_title = i.find_element(By.CLASS_NAME, 'nk-post-title').text
    news_dict['title'] = news_title
    news_date = i.find_element(By.CLASS_NAME, 'nk-post-date').text
    news_dict['date'] = news_date
    news_text = i.find_element(By.CLASS_NAME, 'nk-post-text').text
    news_dict['text'] = news_text
    news_link = i.find_element(By.XPATH, './/a').get_attribute('href')
    finder = db.chromienews.find({'link':{'$eq':news_link}})
    if finder!= news_link:
        news_dict['link'] = news_link     
#adding to database
    db.chromienews.insert_one(news_dict)