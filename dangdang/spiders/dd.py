# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request
# 在cmd上运行


class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=%CC%A4%B2%BD%BB%FA']

    # response就是对request的响应
    def parse(self, response):
        item = DangdangItem()
        item["title"] = response.xpath("//a[@name='itemlist-picture']/@title").extract()
        item["link"] = response.xpath("//a[@name='itemlist-picture']/@href").extract()
        item["price"] = response.xpath("//span[@class='price_n']/text()").extract()
        item["comment"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        # print(item["title"])
        yield item
        for i in range(2, 20):
            url = 'http://search.dangdang.com/?key=%CC%A4%B2%BD%BB%FA&page_index=' + str(i)
            yield Request(url, callback=self.parse)
