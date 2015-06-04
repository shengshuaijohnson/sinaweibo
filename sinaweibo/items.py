from scrapy.item import Item, Field
import scrapy

class Blog(Item):
    text = Field()
    time = Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths=Field()
