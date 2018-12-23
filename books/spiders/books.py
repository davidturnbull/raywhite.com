# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider

class Listing(scrapy.Item):
  url = scrapy.Field()
  status = scrapy.Field()
  html = scrapy.Field()

class ListingSpider(SitemapSpider):
  sitemap_urls = ["https://www.raywhite.com/sitemapindex.xml"]
  sitemap_rules = [
      ("/rwmap_properties_", "parse_listing"),

  def parse_listing(self, response):
    item = Listing()
    item["url"] = response.url
    item["status"] = response.status
    item["html"] = response.text
    return item