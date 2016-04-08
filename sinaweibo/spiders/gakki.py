__author__ = 'Administrator'
# -*- coding: UTF-8 -*-
from scrapy.spider import Spider
import scrapy
from sinaweibo.items import Blog




class GakkiSpider(Spider):
    name = "gakki"
    # allowed_domains = ["http://weibo.com/aragakiyui0611"]
    start_urls = ["http://weibo.com/aragakiyui0611"]

    def load_item(self, d):
        return d
    def parse(self, response):
        site=response.xpath("body").extract()
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'} # Googlebot/2.1
        print "hhhhhhhhhhhhhh"
        yield scrapy.Request("http://weibo.com/aragakiyui0611",
                             callback=self.after_login,
                             headers=user_agent
        )
        
        return
    def after_login(self,response):
        #imgsite=response.xpath('//img[@action-type="fl_pics"]')
        site=response.xpath('/')
        print "aaaaaaaaaaaaaa"
        items=[]
        item=Blog();
        item['text']=site.extract()
        items.append(item)
        """
        for sel in imgsite:
            item = Blog()
            item['image_urls']=sel.xpath('@src').extract() #square  <>bmiddle
            #item['image_urls'][0]=item['image_urls'][0].replace("square","bmiddle")
            items.append(item)
        """
        for d in items:
            yield self.load_item(d)
        return
COOKIES={
        "SINAGLOBAL":"6527430750429.63.1429364749729",
        "wvr":"6",
        "un":"289868795@qq.com",
        "SUS":"SID-1734771015-1452486888-GZ-ksdnh-6709dc10596984702bbbec1db4d7726d",
        " SUE":"es%3Deb4c3780271abca8f1b7365b78cf9136%26ev%3Dv1%26es2%3D6f6cb4b459da2cb23afc4407984eef42%26rs0%3D3ugEldhvztKJaojJ725%252FIHs85kYWYDixyW1Y4869A0wI0p6Vfb%252B%252ByCcAmNXim3g4TG4NP9iq8OBo%252BWJdf4xgBsQb8%252B5eqWUcJna6nzGwm3LN%252BAxsktQ%252BeZglY0qNO6%252FLePW8fviTU009YeucWjPqpf3fGF5PwvZxscCjrfs5hfA%253D%26rv%3D0",
        " SUP":"cv%3D1%26bt%3D1452486888%26et%3D1452573288%26d%3Dc909%26i%3D726d%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D1734771015%26name%3D120559187%2540qq.com%26nick%3D%25E5%25AF%2592%25E6%2598%259F%25E5%2590%25BB%25E6%259C%2588%26fmp%3D%26lcp%3D",
        " SUB":"_2A257l0C4DeTxGedJ6FYW9y_MyjmIHXVY5TVwrDV8PUNbvtBeLUvVkW9LHeuhbgcQ02eh-pZiRaQ_smFkQSvTaw..",
        " SUBP":"0033WrSXqPxfM725Ws9jqgMF55529P9D9WWqayOjQNSyDiXOpBolxJbO5JpX5KMt",
        " SUHB":"0id6luBpF4qrOd",
        " ALF":"1484022888",
        " SSOLoginState":"1452486888",
        " _s_tentry":"login.sina.com.cn",
        " Apache":"8327518606092.781.1452486892279",
        " ULV":"1452486892344:1007:47:3:8327518606092.781.1452486892279:1452484220648",
        " UOR":"www.baicizhan.com,widget.weibo.com,login.sina.com.cn"
}
