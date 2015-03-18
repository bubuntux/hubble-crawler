# -*- coding: utf-8 -*-
import scrapy


class HubbleItem(scrapy.Item):
    name = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()