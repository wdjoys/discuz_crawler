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
            callback="paser_section",
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

        f_name = response.xpath(
            "//body/div[@id='wp']/div[@id='pt']/div[1]/a[4]/text()"
        ).get()

        subject_selectors = response.xpath(
            '//div[@class="bm_c"]//tbody[@id!="separatorline"]/tr'
        )

        data = []  # 主题信息

        for subject_selector in subject_selectors:

            full_title_selector = subject_selector.xpath('th/a[@class="s xst"]')
            subject_title = full_title_selector.xpath("text()").get()
            subject_url = full_title_selector.xpath("@href").get()
            subject_tag = subject_selector.xpath("th/em/a/text()").get()

            # 获取帖子id
            subject_id = re.findall(r"tid=(\d+)", subject_url)[0]  # 不同站点伪静态不同，处理方式不同

            # postby_selector
            post_by_selector = subject_selector.xpath("td[2]")
            subject_author = post_by_selector.xpath("cite/a/text()").get()
            subject_date = post_by_selector.xpath("em/span/span/@title").get()

            if not subject_date:  # 如果属性中没有时间，到文本中提取
                subject_date = post_by_selector.xpath("em/span/text()").get()

            data.append(
                {
                    "title": subject_title,
                    "url": subject_url,
                    "tag": subject_tag,
                    "id": subject_id,
                    "author": subject_author,
                    "date": subject_date,
                    "f_name": f_name,
                }
            )

        # 推出主题信息
        if data:  # 有可能板块内没有帖子，导致报错
            yield {
                "type": "subject",
                "data": data,
                "url": response.url,
            }

    def paser_post(self, response):

        post_selectors = response.xpath('//table[@class="plhin"]/tr[1]')

        data = []  # 帖子信息
        for post_selector in post_selectors:
            content = post_selector.xpath("td[2]/div[@class='pct']//table").get()
            username = post_selector.xpath(
                'td[1]//div[@class="pi"]//div[@class="authi"]/a/text()'
            ).get()
            post_time = (
                post_selector.xpath("td/div/div/div[@class='authi']/em/text()")
                .get()
                .replace("发表于 ", "")
            )

            # 发表于 昨天类似格式处理
            if not post_time:
                post_time = post_selector.xpath(
                    "td/div/div/div[@class='authi']/em/span/@title"
                ).get()

            floor = (
                post_selector.xpath("td[2]/div/strong/a")
                .xpath("string(.)")
                .get()
                .replace("\r\n", "")
            )

            data.append(
                {
                    "content": content,
                    "username": username,
                    "post_time": post_time,
                    "floor": floor,
                    "url": response.url,
                }
            )

        # 推出楼层信息
        if data:  # 有可能帖子没权限，导致报错
            yield {"type": "post", "url": response.url, "data": data}
