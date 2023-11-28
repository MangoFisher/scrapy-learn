import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QidianSpider(CrawlSpider):
    name = "qidian"
    allowed_domains = ["qidian.com"]
    start_urls = ["https://www.qidian.com/xuanhuan/"]

    rules = (Rule(LinkExtractor(allow=r"//www.qidian.com/book/\d+/"), callback="parse_item", follow=False),)

    def parse_item(self, response):
        print(response.url)
        item = {}
        item["url"] = response.url
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item
