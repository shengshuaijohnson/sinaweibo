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


    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', 'spider')

    def load_item(self, d):
        return d

    def parse(self, response):
        print"laaaaaaaaaaaaaaaaaaaaaaaaaaaaaaak"
        user_agent = {'User-agent': 'spider'}  # Mozilla/5.0 (compatible; Googlebot/2.1
        yield scrapy.Request("http://weibo.com/aragakiyui0611",
                             callback=self.after_login,
                             headers=user_agent
                             )

    def after_login(self, response):
        imgsite=response.xpath('//img[@action-type="fl_pics"]')
        items = []
        """
        site = response.xpath('//div[@class="WB_detail"]')
        for sel in site:
            item = Blog()
            item['text'] = sel.xpath('div[@class="WB_text W_f14"]/text()').extract()
            #item['image_urls'] =sel.xpath('div[@class="WB_media_wrap clearfix"]/div/ul/li/img/@src').extract()
            items.append(item)
        """
        for sel in imgsite:
            item = Blog()
            item['image_urls']=sel.xpath('@src').extract() #square  <>bmiddle
            item['image_urls'][0]=item['image_urls'][0].replace("square","bmiddle")
            items.append(item)
        for d in items:
            yield self.load_item(d)
        return