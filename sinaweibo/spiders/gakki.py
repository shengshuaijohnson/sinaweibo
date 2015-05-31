__author__ = 'Administrator'
# -*- coding: UTF-8 -*-
from scrapy.spider import Spider
import scrapy
from sinaweibo.items import Blog  # text.time
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

import re
import requests
class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', 'spider')

class GakkiSpider(Spider):
    name = "gakki"
    #allowed_domains = ["http://weibo.com"]
    start_urls = ["http://weibo.com/aragakiyui0611"]

    def __init__(self, user_agent=''):
        self.user_agent = user_agent
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', 'spider')
    def load_item(self, d):
        return d

    def parse(self, response):
        print"laaaaaaaaaaaaaaaaaaaaaaaaaaaaaaak"
        print response.url
        site=response.xpath("body").extract()
        """items=[]
        for d in site:
            item=Blog()
            item['text']=d
            items.append(item)
        for d in items:
            yield self.load_item(d)
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': '120559187@qq.com', 'password': 'yixuanzyx'},
            callback=self.after_login
        )"""
        user_agent = {'User-agent': 'spider'} # Mozilla/5.0 (compatible; Googlebot/2.1
        yield scrapy.Request("http://weibo.com/aragakiyui0611",
                             callback=self.after_login,
                             headers=user_agent
        )

    def after_login(self, response):
        print "looooooooooooooooooooook"
        site=response.xpath("//text()").extract()
        items=[]
        item=Blog()
        item['text']=site
        items.append(item)
        for d in items:
            yield self.load_item(d)
        return