import scrapy

class JobSpider(scrapy.Spider):
    name = 'job_spider'
    allowed_domains = ['jobs.bytedance.com']
    start_urls = ['https://jobs.bytedance.com/experienced/position']

    def parse(self, response):
        job_detail_links = response.css('a[href^="/experienced/position/"]::attr(href)').extract()

        for link in job_detail_links:
            job_detail_url = response.urljoin(link)
            print(f"Job Detail URL: {job_detail_url}")
            yield scrapy.Request(job_detail_url, callback=self.parse_job_detail)

    def parse_job_detail(self, response):
        # You can further parse the job detail page here if needed
        pass
