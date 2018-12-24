# -*- coding: utf-8 -*-
import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http.request import Request

from wheretolive.items import Listing

class harcourtsSpider(CrawlSpider):
    name = "harcourts"
    allowed_domains = ["harcourts.com.au"]
    start_urls = ["https://harcourts.com.au/Property/Residential", "https://harcourts.com.au/Property/Rentals", "https://harcourts.com.au/Property/Rural" ]

    rules = (
        Rule(LinkExtractor(allow=('\?page=', ))),
        Rule(LinkExtractor(allow=('\d{5}', )), callback='parse_item'),
    )

    def parse_item(self, response):
        item = Listing()
        item["url"] = response.url
        item["status"] = response.status
        item["html"] = response.text
        return item

        