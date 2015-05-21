# -*- coding: UTF-8 -*-
from scrapy.spider import Spider

from sinaweibo.items import Blog  # text.time


class GakkiSpider(Spider):
    name = "gakki"
    allowed_domains = ["http://weibo.com/"]
    start_urls = ["http://weibo.com/aragakiyui0611"]

    def load_item(self, d):
        return d

    def parse(self, response):
        items = []
        item = Blog()

        print "loooooooooooooooooooook"
        sites = response.xpath('//tr')
        for sel in sites:

            item['text']=response.xpath('/div[@class="mcon fl"]/text()').extract()
            items.append(item)
        for d in items:
            yield self.load_item(d)
        return