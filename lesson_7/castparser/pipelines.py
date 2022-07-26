# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient

class CastparserPipeline:
    def __init__(self) -> None:
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.cables

    def process_item(self, item, spider):
#        item['price'] = self.price_corrector(item['price'][0])
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item

#    def price_corrector(price):
#        true_price = []
#        try:
#            int_price = int(price[2].replace(' ', ''))
#            true_price.append(int_price)
#        except:
#            true_price.append(price[2])
#        true_price.append(price[3].replace(' ', ''))
#        return true_price

class CastphotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        #return super().get_media_requests(item, info)
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)
    
    def item_completed(self, results, item, info):
        #return super().item_completed(results, item, info)
        item['photos'] = [itm[1] for itm in results if itm[0]]
        return item