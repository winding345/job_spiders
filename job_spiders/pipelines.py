# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem

class JobSpidersPipeline(object):
    index = 0
    def __init__(self):
        self.file = open('data.csv','w',encoding='utf-8')
    #该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass
    #该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        self.file.close()
        pass
    #该方法用于处理数据
    def process_item(self, item, spider):
        item = dict(item)
        list = []
        if self.index == 0:
            self.file.write(','.join(item.keys()))
            self.index == 1
        for k in item.keys():
            list.append(item[k].replace('\t|\n|\r',''))

        # content = json.dumps(dict(item),ensure_ascii=False) + "\n"
        content = ','.join(item.values())
        self.file.write(content)
        return item
