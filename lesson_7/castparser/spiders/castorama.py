import scrapy
from scrapy.http import HtmlResponse
from items import CastparserItem
from scrapy.loader import ItemLoader
#from selenium import webdriver
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import TimeoutException
#import base64


class CastoramaSpider(scrapy.Spider):
    name = 'castorama'
    allowed_domains = ['castorama.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://www.castorama.ru/electric-appliances/{kwargs.get("search")}/']
        #print(self.start_urls)

    def parse(self, response:HtmlResponse):
#selenium tries
 #       s = Service('./geckodriver')
 #       driver = webdriver.Firefox(service=s)
 #       driver.get(f'https://www.castorama.ru/electric-appliances/cables-and-wires/')
 #       while True:
 #           try:
 #               load_more = WebDriverWait(driver, 30).until(
 #               EC.presence_of_element_located((By.CLASS_NAME, 'product-list-show-more')))
 #               load_more.click()
 #           except TimeoutException:
 #               break

        next_page = response.xpath("//a[contains(@class, 'i-next')]//@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        item_links = response.xpath("//a[contains(@class, 'product-card__img-link')]")
        for link in item_links:
            yield response.follow(link, callback=self.parse_ads)

    
    def parse_ads(self, response:HtmlResponse):
        #kolhoz time!
        price = response.xpath("//div[@class = 'price-box']//text()").getall()
        true_price = []
        try:
            int_price = int(price[2].replace(' ', ''))
            true_price.append(int_price)
        except:
            true_price.append(price[2])
        true_price.append(price[3].replace(' ', ''))
        #kolhoz time over!
        loader = ItemLoader(item=CastparserItem(), response=response)
        loader.add_xpath("name", "//h1/text()")
        loader.add_value("price", true_price)
        loader.add_xpath("photos", "//ul[@class = 'swiper-wrapper']//span/@content")
        loader.add_value("link", response.url)
        yield loader.load_item()


#        name = response.xpath("//h1/text()").get()
        

    
#        link = response.url
#        photos = response.xpath("//ul[@class = 'swiper-wrapper']//span/@content | //img[contains(@class, 'top-slide__img')]/@src").getall()
#        photos = response.xpath("//ul[@class = 'swiper-wrapper']//span/@content").getall()
#        yield CastparserItem(name=name, price=price, link=link, photos=photos)

        
        

        
        

  
