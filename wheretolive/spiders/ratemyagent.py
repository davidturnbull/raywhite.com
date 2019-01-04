# -*- coding: utf-8 -*-
import scrapy
import re
import urllib
from scrapy.spiders import SitemapSpider
from wheretolive.items import Listing

class ratemyagentAgencySpider(SitemapSpider):
    name = "ratemyagent_agencies"
    allowed_domains = ["ratemyagent.com.au"]
    sitemap_urls = ["https://www.ratemyagent.com.au/sitemap.xml"]
    sitemap_follow = ["sitemap-agencies"]
    sitemap_rules = [
        ('/reviews', 'parse_agency')
    ]

    # https://www.ratemyagent.com.au/sitemap.xml
    # https://api.ratemyagent.com.au/Agencies/Code-ap640

    def parse_agency(self, response):

        # Extract the agency ID from the URL
        agency_id = re.search('-(\w+\d+)\/', response.url).group(1)
        api_url = "https://api.ratemyagent.com.au/Agencies/Code-" + agency_id

        item = Agency()
        item["url"] = response.url
        item["status"] = response.status
        item["html"] = response.text
        item["json"] = urllib.urlopen(api_url).read()
        yield item