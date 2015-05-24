__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from sinaweibo.items import Blog
from scrapy.http import Request


def load_item(d):
    return d


class Zhihuspider(Spider):
    name = "zhihu"
    # allowed_domains = ["http://www.zhihu.com/"]
    start_urls = [
        "http://www.zhihu.com/#signin"
    ]

    def parse(self, response):
        site = response.xpath("//text()").extract()
        item = Blog()
        item["text"] = site

        if response.url == "http://www.zhihu.com/":
            yield Request("http://bbs.sgamer.com/forum-44-2.html", callback=self.parse)
        yield load_item(item)
        return
