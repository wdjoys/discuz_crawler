"""
Author: wdjoys
Date: 2022-04-19 11:15:07
LastEditors: wdjoys
LastEditTime: 2022-04-21 14:45:34
FilePath: \discuz_crawler\discuz\discuz\start.py
Description: 

Copyright (c) 2022 by github/wdjoys, All Rights Reserved. 
"""
import sys

ISDEBUG = bool(sys.gettrace())
print(ISDEBUG)


from scrapy.cmdline import execute

from settings import ISDEBUG

if ISDEBUG:
    print("Debug模式启动")
    execute("scrapy crawl discuz_crawler".split())
else:
    print("工作模式启动")
    execute("scrapy crawl discuz_crawler -s JOBDIR=cache".split())
