__author__ = 'Administrator'
# -*- coding: UTF-8 -*-
from scrapy.spider import Spider
import scrapy
from sinaweibo.items import Blog
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware




class GakkiSpider(Spider):
    name = "gakki" 
    # allowed_domains = ["http://weibo.com/aragakiyui0611"]
    start_urls = ["http://weibo.com/aragakiyui0611"]

    def __init__(self, user_agent=''):
        self.user_agent = user_agent
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', 'spider')

    def load_item(self,d):
        return d

    def parse(self, response):
        user_agent = {'User-agent': 'spider'}
        yield scrapy.Request("http://weibo.com/aragakiyui0611",
                             callback=self.after_login,
                             headers=user_agent
        )
        print "hhhhhhhhhhhhhh"
        return
    def after_login(self,response):
        print "jjjjjjjjjjjjjjjjjj"
 
        imgsite=response.xpath('//img/@src')
        items=[]
        for sel in imgsite:
            item = Blog()
            url=sel.extract()
            url=url.replace('thumb180','mw690')
            url=url.replace('orj480','mw690')
            item["image_urls"] = url
            items.append(item)
            #item['image_urls'][0]=item['image_urls'][0].replace("square","bmiddle")
        for d in items:
            yield self.load_item(d)
        return
