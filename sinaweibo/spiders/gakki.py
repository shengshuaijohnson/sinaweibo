__author__ = 'Administrator'
# -*- coding: UTF-8 -*-
from scrapy.spider import Spider
import scrapy
from sinaweibo.items import Blog
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware


class RotateUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', 'Googlebot/2.1')


class GakkiSpider(Spider):
    name = "gakki"
    # allowed_domains = ["http://weibo.com"]
    start_urls = ["http://www.zhihu.com/"]

    def load_item(self, d):
        return d

    def parse(self, response):
        print"laaaaaaaaaaaaaaaaaaaaaaaaaaaaaaak"
        user_agent = {'User-agent': 'Googlebot/2.1'}  # Mozilla/5.0 (compatible; Googlebot/2.1
        yield scrapy.Request("http://www.zhihu.com/",
                             callback=self.after_login,
                             headers=user_agent
                             )

    def after_login(self, response):
        print "jjooooooooooooooooooooo"
        print response.url
        imgsite=response.xpath('//img[@action-type="fl_pics"]')
        solo=response.xpath('//img[@node-type="feed_list_media_bgimg"]')
        imgsite.append(solo)
        x=response.xpath('//text()').extract()
        print str(x)
        """
        site = response.xpath('//div[@class="WB_detail"]')
        for sel in site:
            item = Blog()
            item['text'] = sel.xpath('div[@class="WB_text W_f14"]/text()').extract()
            #item['image_urls'] =sel.xpath('div[@class="WB_media_wrap clearfix"]/div/ul/li/img/@src').extract()
            items.append(item)
        """
        """
        for sel in imgsite:
            item = Blog()
            item['image_urls']=sel.xpath('@src').extract() #square  <>bmiddle
            item['image_urls'][0]=item['image_urls'][0].replace("square","bmiddle")
            items.append(item)
        for d in items:
            yield self.load_item(d)
        """
        return