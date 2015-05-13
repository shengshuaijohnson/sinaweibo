from scrapy.item import Item, Field


class Blog(Item):
    text = Field()
    time = Field()
