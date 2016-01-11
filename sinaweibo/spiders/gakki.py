__author__ = 'Administrator'
# -*- coding: UTF-8 -*-
from scrapy.spider import Spider
import scrapy
from sinaweibo.items import Blog
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware


class RotateUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', 'spider')


class GakkiSpider(Spider):
    name = "gakki"
    # allowed_domains = ["http://weibo.com"]
    start_urls = ["http://weibo.com/aragakiyui0611"]

    def load_item(self, d):
        return d

    def parse(self, response):
        user_agent = {'User-agent': 'spider'}  # Mozilla/5.0 (compatible; Googlebot/2.1
        yield scrapy.Request("http://weibo.com/aragakiyui0611?is_search=0&visible=0&is_tag=0&profile_ftype=1&page=1#feedtop",
                             callback=self.after_login,
                             headers=user_agent
                             )

    def after_login(self, response):
        print "jooooooooooooooooooooooooo!"
        print response.xpath('//')
        
        """
        imgsite=response.xpath('//img[@action-type="fl_pics"]')
        solo=response.xpath('//img[@node-type="feed_list_media_bgimg"]')
        imgsite.append(solo)
        print solo
        imgsite=response.xpath('//img')
        items = []

        for sel in imgsite:
            item = Blog()
            item['image_urls']=sel.xpath('@src').extract() #square  <>bmiddle
            #item['image_urls'][0]=item['image_urls'][0].replace("square","bmiddle")
            items.append(item)
        for d in items:
            yield self.load_item(d)
        """
        return