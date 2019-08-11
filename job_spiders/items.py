# -*- coding: utf-8 -*-
# 此处定义你要进行获取的数据内容标题

import scrapy


class JobSpidersItem(scrapy.Item):
    # define the fields for your item here like:
    #公司名字
    cname = scrapy.Field()
    #职位名字
    pname = scrapy.Field()
    #薪水
    salary = scrapy.Field()
    # 详情链接
    dlink = scrapy.Field()

    # 工作地点
    workplace = scrapy.Field()
    # 工作经验
    experience = scrapy.Field()
    # 学历
    education = scrapy.Field()
    #发布时间
    publictime = scrapy.Field()

    # 公司福利
    welfare = scrapy.Field()

    #任职要求
    requirement = scrapy.Field()

    #公司类型
    ctype = scrapy.Field()
    #公司规模
    scale = scrapy.Field()
    #公司性质
    nature = scrapy.Field()

