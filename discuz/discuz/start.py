"""
Author: wdjoys
Date: 2022-04-19 11:15:07
LastEditors: wdjoys
LastEditTime: 2022-04-19 11:15:08
FilePath: \discuz_crawler\discuz\discuz\start.py
Description: 

Copyright (c) 2022 by github/wdjoys, All Rights Reserved. 
"""

from scrapy.cmdline import execute

execute("scrapy crawl discuz_crawler".split())
