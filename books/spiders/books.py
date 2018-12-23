
# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider

class ListingSpider(SitemapSpider):
  name = "books"
  allowed_domains = ["raywhite.com"]
  sitemap_urls = ["https://www.raywhite.com/sitemapindex.xml"]
  sitemap_rules = [
      ("/rwmap_properties_", "parse_listing"),
  ]

  def parse_listing(self, response):
    item = {}
    item["url"] = response.url
    item["status"] = response.status
    item["html"] = response.text
    yield item