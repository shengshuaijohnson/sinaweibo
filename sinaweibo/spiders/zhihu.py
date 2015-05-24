__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from scrapy.spider import Spider
import scrapy
from sinaweibo.items import Blog

class Zhihuspider(Spider):
    name = "zhihu"
    allowed_domains = ["http://www.zhihu.com/"]
    start_urls = [
        "http://www.zhihu.com/"
    ]

    def parse(self, response):
        site = response.body
        item=Blog()
        item["text"]=site
        return item
