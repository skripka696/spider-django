# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from web_app.tasks import choice_spider


class SpiderPipeline(object):
    def __init__(self):
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def process_item(self, item, spider):
        self.items.append(item._values)
        if len(self.items) >= 1000:
            # choice_spider(spider.__class__.name, items=self.items)
            choice_spider.delay(spider.__class__.name, item=self.items)
        return item

    def spider_closed(self, spider):
        if self.items:
            # choice_spider(spider.__class__.name, items=self.items)
            choice_spider.delay(spider.__class__.name, items=self.items)