from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import time

s = Service('./geckodriver')
options = Options()
#options.add_argument('start-maximized')
driver = webdriver.Firefox(service=s)

driver.get('https://www.chromiecraft.com/en/news/')

cookie_button = driver.find_element(By.CLASS_NAME, 'tibrr-cookie-consent-button')
time.sleep(4)
try:
    cookie_button.click()
except:
    pass
time.sleep(4)
#driver.execute_script('window.scrollTo(1, document.body.scrollHeight);')

paginator = driver.find_element(By.LINK_TEXT, 'Load More')
time.sleep(4)
paginator.click
#actions = ActionChains(driver)
#time.sleep(6)
#actions.move_to_element(paginator).perform()
#pagination_button.click()