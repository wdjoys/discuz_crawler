"""
Author: wdjoys
Date: 2022-04-21 08:11:53
LastEditors: wdjoys
LastEditTime: 2022-05-07 09:32:13
FilePath: \discuz_crawler\discuz\discuz\pipelines.py
Description: 

Copyright (c) 2022 by github/wdjoys, All Rights Reserved. 
"""


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from urllib.parse import urlparse
from itemadapter import ItemAdapter

import pymongo
import scrapy
from scrapy.pipelines.images import ImagesPipeline

from settings import ISDEBUG


class DiscuzPipeline:
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host="localhost", port=27017)
        # pass

    def process_item(self, item, spider):
        if ISDEBUG:
            return item

        if item["type"] in ["user", "post", "subject"]:
            self.client.geem2bbs[item["type"]].insert_many(item["data"])
        return item

    def close_spider(self, spider):
        self.client.close()
        # pass


class DiscuzImagesPipeline(ImagesPipeline):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_media_requests(self, item, info):

        if item["type"] == "img":
            for image_url in item["data"]:
                yield scrapy.Request(image_url)

    def file_path(self, request, response=None, info=None):
        parse_result = urlparse(request.url)
        path = parse_result.path
        basename = os.path.basename(path)
        return basename
