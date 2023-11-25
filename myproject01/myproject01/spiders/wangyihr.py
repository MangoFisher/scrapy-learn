import scrapy
import json
from ..items import WangyiItem


class WangyihrSpider(scrapy.Spider):
    name = 'wangyihr'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/job-list.html']

    def __init__(self, *args, **kwargs):
        super(WangyihrSpider, self).__init__(*args, **kwargs)
        self.current_page = 1

    def parse(self, response):
        # 获取异步请求所需的参数
        csrf_token = response.css('meta[name="csrf-token"]::attr(content)').get()
        url = 'https://hr.163.com/api/hr163/position/queryPage'

        # 构造异步请求
        yield scrapy.Request(
            url,
            method='POST',
            headers={'Content-Type': 'application/json'},
            body=json.dumps({'pageSize': 10, 'currentPage': 1}),
            callback=self.parse_jobs
        )

    def parse_jobs(self, response):
        # 处理异步请求的响应
        data = json.loads(response.body)
        job_list = data.get('data', {}).get('list', [])
        print(len(job_list))

        for job in job_list:
            item = WangyiItem()
            item['name'] = job.get('name', '')
            item['workPlaceNameList'] = job.get('workPlaceNameList', [])
            item['firstDepName'] = job.get('firstDepName', '')
            item['recruitNum'] = job.get('recruitNum', '')
            print(item)
            yield item

        # 获取总页数
        total_pages = data.get('data', {}).get('pages', 1)


        # 如果还有下一页，继续发送请求
        if self.current_page < total_pages:
            self.current_page += 1
            next_url = 'https://hr.163.com/api/hr163/position/queryPage'
            yield scrapy.Request(
                next_url,
                method='POST',
                headers={'Content-Type': 'application/json'},
                body=json.dumps({'pageSize': 10, 'currentPage': self.current_page}),
                callback=self.parse_jobs,
                meta={'current_page': self.current_page}
            )


