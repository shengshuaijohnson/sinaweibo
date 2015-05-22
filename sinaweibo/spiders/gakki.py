# -*- coding: UTF-8 -*-
from scrapy.spider import Spider
import scrapy
from sinaweibo.items import Blog  # text.time


class GakkiSpider(Spider):
    name = "gakki"
    allowed_domains = ["http://bbs.sgamer.com"]
    start_urls = ["http://bbs.sgamer.com/forum-44-1.html"]#妈个比，微博换SG就不会出现没有form元素了

    def load_item(self, d):
        return d

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': '120559187@qq.com', 'password': 'yixuanzyx'},
            callback=self.after_login
        )

    def after_login(self, response):
        print "looooooooooooooooooooook"
        print response.body
        # items=[]
        #for d in items:
        #    yield self.load_item(d)
        return