# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MetadatascraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    #author = scrapy.Field()
    pdf = scrapy.Field()
    download = scrapy.Field()
    catalogItem = scrapy.Field()
    otherLinks = scrapy.Field()
    webUrl = scrapy.Field()
    abstractCount = scrapy.Field()
    # abstractMissing = scrapy.Field()
    identifier = scrapy.Field()