"""
Author: wdjoys
Date: 2022-04-19 09:55:40
LastEditors: wdjoys
LastEditTime: 2022-04-20 16:11:42
FilePath: \discuz_crawler\discuz\discuz\pipelines.py
Description: 

Copyright (c) 2022 by github/wdjoys, All Rights Reserved. 
"""


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DiscuzPipeline:
    def opene_spider(self, spider):

        pass

    def process_item(self, item, spider):
        print(item)
        return item

    def close_spider(self, spider):
        pass
