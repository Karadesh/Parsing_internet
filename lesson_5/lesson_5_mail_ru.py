from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

s = Service('./geckodriver')
options = Options()
#options.add_argument('start-maximized')
driver = webdriver.Firefox(service=s)

driver.get('https://account.mail.ru/login')
time.sleep(4)
login = driver.find_element(By.CLASS_NAME, 'input-0-2-77')
time.sleep(6)
login.send_keys('study.ai_172')
time.sleep(6)
submit = driver.find_element(By.CLASS_NAME, 'submit-button-wrap')
try:
    submit.click()
except:
    time.sleep(4)
time.sleep(4)
password = driver.find_element(By.NAME, 'password')
time.sleep(4)
password.send_keys('NextPassword172#')
time.sleep(6)
try:
    submit.click()
except:
    time.sleep(4)



