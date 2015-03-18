# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor

from scrapy.contrib.spiders import Rule, CrawlSpider

from Hubble.items import HubbleItem


class SpaceTelescopeSpider(CrawlSpider):
    name = "SpaceTelescope"
    allowed_domains = ["spacetelescope.org"]
    start_urls = (
        'http://www.spacetelescope.org/images/archive/search/?adv=&type=Observation&minimum_size=8&wallpapers=on',
    )
    rules = (Rule(LxmlLinkExtractor(restrict_xpaths='//span[contains(@class, "paginator_next")]/a'), callback='parse', follow=True),)

    def parse(self, response):
        items = []
        for td in response.selector.css('.imagerow'):
            name = td.css('img::attr(alt)').extract()[0]
            url = 'http://www.spacetelescope.org/static/archives/images/wallpaper5/' + td.css('a::attr(href)').extract()[0][8:-1] + '.jpg'
            items.append(HubbleItem(name=name, image_urls=[url]))
        return items