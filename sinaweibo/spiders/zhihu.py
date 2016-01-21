__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from sinaweibo.items import Blog
import scrapy
from scrapy.http import Request


def load_item(d):
    return d


class Zhihuspider(Spider):
    name = "zhihu"
    # allowed_domains = ["http://www.zhihu.com/"]
    start_urls = [
        "http://weibo.com/aragakiyui0611"
    ]

    def parse(self, response):
        print"loooooooooooooooooooooook"
        print response.url
        site = response.xpath('//text()').extract()
        items = []
        for sel in site:
            if len(sel) > 1:
                item = Blog()
                item["text"] = sel
                items.append(item)
        item = Blog()
        item["text"] = response.url
        print response.url.split("/")[-2]
        for d in items:
            yield load_item(d)
        return
