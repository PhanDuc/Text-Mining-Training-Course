# -*- coding: utf-8 -*-

import scrapy

class WebContentSpider(scrapy.Spider):
    name = "webcontent"
    start_urls = [
        "https://techcrunch.com/2013/08/15/panorama-education-wants-to-make-polling-parents-students-and-teachers-easier-for-educators/"
    ]
    allowed_domains = ["techcrunch.com"]

    def parse(self, response):
        items = {}
        ps = []
        for p_node in response.xpath('//div[@class="article-entry text"]/p/text()'):
            ps.append( p_node.extract() )
        items['content'] = '\n'.join(ps)
        yield items
