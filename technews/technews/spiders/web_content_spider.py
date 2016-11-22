# -*- coding: utf-8 -*-

import scrapy

class WebContentSpider(scrapy.Spider):
    name = "webcontent"
    start_urls = [
        "https://techcrunch.com/2013/08/15/panorama-education-wants-to-make-polling-parents-students-and-teachers-easier-for-educators/",
        "https://techcrunch.com/2016/11/19/how-data-science-and-rocket-science-will-get-humans-to-mars",
        "https://techcrunch.com/2016/11/16/microsoft-offers-concessions-to-eu-regulators-eyeing-its-26-2bn-linkedin-bid/"
    ]

    def parse(self, response):
        items = {}
        items['link'] = response.url
        ps = []
        for p_node in response.xpath('//div[@class="article-entry text"]/p/text()'):
            ps.append( p_node.extract() )
        items['content'] = ' '.join(ps)
        yield items
