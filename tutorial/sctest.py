import scrapy
from scrapy.crawler import CrawlerProcess


class MySpider(scrapy.Spider):
    name = "MySpider"

    def start_requests(self):

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
		
		for x in xpaths:
			print response.xpath(x)