# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    contribution_name = scrapy.Field()
    address = scrapy.Field()
    contributor_type = scrapy.Field()
    candidate_name = scrapy.Field()
    state = scrapy.Field()
    amount = scrapy.Field()
    transaction_date = scrapy.Field()
