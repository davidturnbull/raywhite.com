
# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider

class Listing(scrapy.Item):
    url = scrapy.Field()
    status = scrapy.Field()
    html = scrapy.Field()

class raineandhorneSpider(SitemapSpider):
  name = "raineandhorne"
  allowed_domains = ["raineandhorne.com.au"]
  sitemap_urls = ["https://www.raineandhorne.com.au/sitemaps/sitemap-rentals.xml.gz"]
  sitemap_follow = ["sitemap-rentals", "sitemap-buy"]

  def parse(self, response):
    item = Listing()
    item["url"] = response.url
    item["status"] = response.status
    item["html"] = response.text
    yield item