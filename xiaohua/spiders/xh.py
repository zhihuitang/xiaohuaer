# -*- coding: utf-8 -*-
import scrapy
from xiaohua.items import PicItem


class XhSpider(scrapy.Spider):
    # 爬虫名称，唯一
    name = "xh"
    # 允许访问的域
    allowed_domains = ["xiaohuar.com"]
    # 初始URL
    start_urls = ['http://www.xiaohuar.com/list-1-2.html']

    def parse(self, response):
        # 获取所有图片的a标签
        allPics = response.xpath('//div[@class="img"]/a')
        for pic in allPics:
            item = PicItem()
            name = pic.xpath('./img/@alt').extract()[0]
            addr = pic.xpath('./img/@src').extract()[0]
            if addr.startswith('/'):
                addr = 'http://www.xiaohuar.com' + addr

            item['name'] = name
            item['addr'] = addr
            # 返回爬取到的数据
            yield item
