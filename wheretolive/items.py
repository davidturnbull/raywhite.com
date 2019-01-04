# -*- coding: utf-8 -*-

import scrapy

class Listing(scrapy.Item):
    url = scrapy.Field()
    status = scrapy.Field()
    html = scrapy.Field()

class Agency(scrapy.Item):
    url = scrapy.Field()
    status = scrapy.Field()
    html = scrapy.Field()
    json = scrapy.Field()

class Agent(scrapy.Item):
    url = scrapy.Field()
    status = scrapy.Field()
    html = scrapy.Field()