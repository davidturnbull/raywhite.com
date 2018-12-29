# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider
from wheretolive.items import Agency

class realestateAgencySpider(SitemapSpider):
  name = "realestate_agencies"
  allowed_domains = ["realestate.com.au"]
  sitemap_urls = ["https://www.realestate.com.au/agency/sitemap.xml"]

  def parse(self, response):
    item = Agency()
    item["url"] = response.url
    item["status"] = response.status
    item["html"] = response.text
    yield item