# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="dd")
        for i in range(0, len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            price = item["price"][i]
            comment = item["comment"][i]
            # print(title + "：" + link + "：" + price + "：" + comment)
            sql = "insert into goods(title, link, price, comment) values('"+title+"', '"+link+"', '"+price+"', '"+comment+"')"
            # print(sql)
            try:
                conn.query(sql)
            except Exception as err:
                print(err)
        conn.close()
        return item
