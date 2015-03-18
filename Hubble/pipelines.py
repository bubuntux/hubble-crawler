# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.contrib.pipeline.images import ImagesPipeline


class HubblePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        return request.meta['name'].replace('/', '-') + '.jpg'

    def get_media_requests(self, item, info):
        return [Request(x, meta={'name': item['name']}) for x in item.get(self.IMAGES_URLS_FIELD, [])]