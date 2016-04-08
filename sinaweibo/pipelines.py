

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy
import json
import codecs


class SinaweiboPipeline(object):
    def __init__(self):
	    self.file = codecs.open('items.json', 'w', encoding='utf-8')
    def process_item(self,item,spider):
        line=json.dumps(dict(item))+"\n"
        self.file.write(line.decode('unicode_escape'))
        return item
class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):

        print"ppppppppppppppppppppppppp"
        print item['image_urls']
        yield scrapy.Request(item['image_urls'])
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            print "nooooooooooooooooooooooo"
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
