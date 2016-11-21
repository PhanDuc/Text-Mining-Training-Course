# -*- coding: utf-8 -*-

import scrapy

class BigDataSpider(scrapy.Spider):
    name = "bigdata"
    start_urls = [
        "https://techcrunch.com/tag/big-data"
    ]
    allowed_domains = ["techcrunch.com"]

    def parse(self, response):
        items = {}
        for link_node in response.xpath('//h2[@class="post-title"]/a'):
            items['post-title'] = link_node.xpath('./text()').extract_first()
            items['href'] = link_node.xpath('@href').extract_first()
            yield items

        # go to the next page
        next_page_url = response.xpath('//ol[@class="pagination"]/li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
