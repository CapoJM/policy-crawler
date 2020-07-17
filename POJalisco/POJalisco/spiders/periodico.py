# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class PeriodicoSpider(CrawlSpider):
    name = 'periodico'
    allowed_domains = ['periodicooficial.jalisco.gob.mx']
    start_urls = ['https://periodicooficial.jalisco.gob.mx/periodicos/periodico-oficial/']
    rules = (Rule(LinkExtractor(allow=(), restrict_css=('.pager-next',)), callback="parse_item", follow=True),)

    def parse_item(self, response):
        print('Processing: '+response.url)
