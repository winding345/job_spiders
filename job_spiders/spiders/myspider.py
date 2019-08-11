# -*- coding: utf-8 -*-

import scrapy
#从items文件里导入JobSpidersItem，作为存储相应的结果
from job_spiders.items import JobSpidersItem

class MySpider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = ['51job.com']
    page_index = 1
    url = "https://search.51job.com/list/080200%252C00,000000,0000,00,9,99,%2B,2,{0}.html"
    start_urls = [url.format(page_index)]

    def parse(self,response):
        item = JobSpidersItem()
        #获取该页面上的所有招聘岗位地址
        urls = response.xpath('//div/p/span/a/@href').extract()
        #遍历进入这些地址，获取哥哥岗位的数据信息
        for url in urls:
           yield scrapy.Request(url,callback=self.parse_detail)#callback即回调函数

        #由于岗位页面数量只有2000个，所有要判断一下
        if self.page_index < 2 :
            self.page_index += 1
            #去下一页再去获取对应的岗位数据
            yield scrapy.Request(self.url,callback=self.parse)


    def parse_detail(self,response):
        item = JobSpidersItem()
        item["salary"] = response.xpath('//div[@class="tHeader tHjob"]/div/div/strong/text()').extract()[0]
        item["cname"] = response.xpath('//p[@class="cname"]/a/@title').extract()[0]
        item["pname"] = response.xpath('//h1/text()').extract()[0]
        item["dlink"] = response.url
        msg_ltype = response.xpath('//p[@class="msg ltype"]/@title').extract()[0]
        #去除网页编码多出来的无效字符\xa0
        list = msg_ltype.replace('\xa0','').split('|')
        item["workplace"],item["experience"] = list[:2]
        item["publictime"] = list[-1]
        #有些发布没有写学历要求，需要筛选一下
        item["education"] = list[2] if len(list) == 5 else "没有学历要求"
        item["welfare"] = '，'.join(response.xpath('//div[@class="jtag"]/div/span/text()').extract())
        item["requirement"] = ';'.join(response.xpath('//div[@class="bmsg job_msg inbox"]/p/text()').extract()).replace('\xa0','')
        item["nature"] = response.xpath('//div[@class="com_tag"]/p/span[@class="i_flag"]/../text()').extract()[0]
        item["scale"] = response.xpath('//div[@class="com_tag"]/p/span[@class="i_people"]/../text()').extract()[0]
        item["ctype"] = response.xpath('//div[@class="com_tag"]/p/span[@class="i_trade"]/../@title').extract()[0]
        yield item