"""
Author: wdjoys
Date: 2022-04-20 09:21:26
LastEditors: wdjoys
LastEditTime: 2022-04-20 15:53:06
FilePath: \discuz_crawler\discuz\discuz\spiders\discuz_crawler.py
Description: 

Copyright (c) 2022 by github/wdjoys, All Rights Reserved. 
"""
"""
Author: wdjoys
Date: 2022-04-20 09:21:26
LastEditors: wdjoys
LastEditTime: 2022-04-20 09:55:52
FilePath: \discuz_crawler\discuz\discuz\spiders\discuz_crawler.py
Description: 

Copyright (c) 2022 by github/wdjoys, All Rights Reserved. 
"""
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class DiscuzCrawlerSpider(CrawlSpider):
    name = "discuz_crawler"
    allowed_domains = ["cqscyd.com"]
    start_urls = ["http://www.cqscyd.com"]

    rules = (
        Rule(LinkExtractor(allow=r"Items/"), callback="l", follow=True),
        # 板块连接
        Rule(
            LinkExtractor(restrict_xpaths=(r"//table/tr/td/dl/dt/a",)),
            callback="paser_section",
            follow=True,
        ),
        # 文章连接
        Rule(
            LinkExtractor(restrict_xpaths=(r'//a[@class="s xst"]',)),
            callback="paser_post",
            follow=True,
        ),
        # 文章下一页
        Rule(
            LinkExtractor(
                allow=r"tid=\d+", restrict_xpaths=(r'(//a[@class="nxt"])[2]',)
            ),
            callback="paser_post",
            follow=True,
        ),
        # 文章列表下一页
        Rule(
            LinkExtractor(
                allow=r"fid=\d+", restrict_xpaths=(r'(//a[@class="nxt"])[2]',)
            ),
            follow=True,
        ),
    )

    def login(self, response):
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    def paser_section(self, response):
        print(response)

    def paser_post(self, response):
        full_title_selector = response.xpath('//h1[@class="ts"]')
        subject_name = full_title_selector.xpath("span/text()").get()
        subject_tag = full_title_selector.xpath("a/text()").get()
        subject_url = response.url
        subject_id = re.findall(r"tid=(\d+)", subject_url)[0]

        # 推出主题信息
        yield {
            "type": "subject",
            "data": {
                "subject_name": subject_name,
                "subject_tag": subject_tag,
                "subject_id": subject_id,
                "subject_url": subject_url,
            },
        }

        post_selectors = response.xpath('//table[@class="plhin"]/tr[1]')
        for post_selector in post_selectors:
            content = post_selector.xpath("td[2]/div[@class='pct']").get()
            username = post_selector.xpath(
                'td[1]//div[@class="pi"]//div[@class="authi"]/a/text()'
            ).get()
            post_time = post_selector.xpath("//em[@id]/text()").get()
            floor = (
                post_selector.xpath("td[2]/div/strong/a")
                .xpath("string(.)")
                .get()
                .replace("\r\n", "")
            )

            # 推出楼层信息
            yield {
                "type": "post",
                "data": {
                    # "content": content,
                    "username": username,
                    "post_time": post_time,
                    "floor": floor,
                    "subject_url": subject_url,
                },
            }
