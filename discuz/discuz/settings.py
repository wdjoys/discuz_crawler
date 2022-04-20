"""
Author: wdjoys
Date: 2022-04-19 09:55:40
LastEditors: wdjoys
LastEditTime: 2022-04-19 11:00:54
FilePath: \discuz_crawler\discuz\discuz\settings.py
Description: 

Copyright (c) 2022 by github/wdjoys, All Rights Reserved. 
"""
# Scrapy settings for discuz project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "discuz"

SPIDER_MODULES = ["discuz.spiders"]
NEWSPIDER_MODULE = "discuz.spiders"

LOG_LEVEL = "ERROR"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "Cookie": "Z1VD_2132_saltkey=VW75g84M; Z1VD_2132_lastvisit=1650414236; Z1VD_2132_study_nge_extstyle=auto; Z1VD_2132_study_nge_extstyle_default=auto; Z1VD_2132_atarget=1; Z1VD_2132_st_t=0%7C1650445608%7Cf5decdd630d0d82856c71f511fbefccc; Z1VD_2132_forum_lastvisit=D_116_1650443083D_39_1650445608; Z1VD_2132_sendmail=1; Z1VD_2132_seccode=142.067a756a788f8f9a26; Z1VD_2132_ulastactivity=5b6elpLGFL0N2p%2BgesfGfyHUsUPXKfy4jpFZmk2QP0tXNiyNzaEi; Z1VD_2132_auth=4fcbxoPTfpbPOYrbpklNnVqmkS7D7RjkpkfxJ1shbKXpQ1OZqy8Bhmiw8doEwwOFFA6jjRV%2FHnRy%2Fv15IwvISy22; Z1VD_2132_lastcheckfeed=3915%7C1650446259; Z1VD_2132_checkfollow=1; Z1VD_2132_st_p=3915%7C1650446261%7C1ca7ae52b67c87a764626feca3142c6d; Z1VD_2132_visitedfid=60D39D116D85; Z1VD_2132_viewid=tid_75361; Z1VD_2132_smile=1D1; Z1VD_2132_sid=SspThV; Z1VD_2132_lip=14.135.74.25%2C1650446261; Z1VD_2132_lastact=1650446263%09home.php%09spacecp; Z1VD_2132_checkpm=1",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'discuz.middlewares.DiscuzSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'discuz.middlewares.DiscuzDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "discuz.pipelines.DiscuzPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
