# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider
from wheretolive.items import Listing

class allhomesListingSpider(SitemapSpider):
    name = "allhomes_listings"
    allowed_domains = ["allhomes.com.au"]
    sitemap_urls = ["https://www.allhomes.com.au/listings.xml"]
    sitemap_follow = ["listings"]

    def parse(self, response):
        item = Listing()
        item["url"] = response.url
        item["status"] = response.status
        item["html"] = response.text
        yield item