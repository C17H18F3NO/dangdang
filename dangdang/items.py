# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 作为标题的容器
    title = scrapy.Field()
    # 作为链接的容器
    link = scrapy.Field()
    # 作为价格的容器
    price = scrapy.Field()
    # 作为评论数的容器
    comment = scrapy.Field()
