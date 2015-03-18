# -*- coding: utf-8 -*-

BOT_NAME = 'Hubble'

SPIDER_MODULES = ['Hubble.spiders']
NEWSPIDER_MODULE = 'Hubble.spiders'

ITEM_PIPELINES = {'Hubble.pipelines.HubblePipeline': 1}
IMAGES_STORE = 'CHANGE_ME'  # TODO use ${HOME}/Pictures/Hubble