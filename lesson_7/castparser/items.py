# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst
#from itemloaders.processors import Identity


class CastparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field()
    photos = scrapy.Field()
    link = scrapy.Field(output_processor=TakeFirst())

