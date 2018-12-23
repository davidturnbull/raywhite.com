
# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider

class Listing(scrapy.Item):
    url = scrapy.Field()
    status = scrapy.Field()
    html = scrapy.Field()

class raywhiteSpider(SitemapSpider):
  name = "raywhite"
  allowed_domains = ["raywhite.com"]
  sitemap_urls = ["https://www.raywhite.com/sitemapindex.xml"]
  sitemap_follow = ["/rwmap_properties"]

  def parse(self, response):
    item = Listing()
    item["url"] = response.url
    item["status"] = response.status
    item["html"] = response.text
    yield item