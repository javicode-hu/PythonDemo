# -*- coding: utf-8 -*-
import mysql.connector
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MysqlPipeline(object):

    def process_item(self, item, spider):
        name = item.get('name')
        author = item.get('author')
        # novelurl = item.get('novelurl')
        category = item.get('category')
        name_id = item.get('name_id')
        content = name+" "+author+" "+name_id+"\n"
        with open("{}.txt".format(category),'a',encoding="utf-8") as f:
            f.write(content)
            f.close()
        return item

