import scrapy
from scrapy.http import HtmlResponse


class CastoramaSpider(scrapy.Spider):
    name = 'castorama'
    allowed_domains = ['castorama.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://www.castorama.ru/electric-appliances/{kwargs.get("search")}/']
        print(self.start_urls)

    def parse(self, response:HtmlResponse):
        item_links = response.xpath("//a[contains(@class, 'product-card__img-link')]//@href")
        print(item_links)
        for link in item_links:
            yield response.follow(link)
            #print(response.url)
        

  
