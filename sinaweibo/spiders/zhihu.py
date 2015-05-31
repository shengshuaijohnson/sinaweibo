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
        "http://www.zhihu.com/#signin"
    ]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata=dict(email='120559187@qq.com', password='yixuanzyx'),
            callback=self.after_login
        )

    def after_login(self, response):
        print"loooooooooooooooooooooook"
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
        if response.url == "http://www.zhihu.com/":
            yield Request("http://weibo.com/", callback=self.after_login)
        for d in items:
            yield load_item(d)
        return
