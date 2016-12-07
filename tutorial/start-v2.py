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

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

#dane wejsciowe:
urls = [
	"http://allegro.pl/6-i-2002-2008-147321?a_text_i%5B14%5D%5B0%5D=140&a_enum%5B16%5D%5B1%5D=1&a_enum%5B16%5D%5B4%5D=4&a_enum%5B13%5D%5B3%5D=3&price_to=12000&a_text_i%5B4%5D%5B1%5D=190000&a_enum%5B128790%5D%5B2%5D=2&a_enum%5B178%5D%5B1%5D=1",
]
xpath = "//h2[@class='offer-header']/a | //h2[@class='offer-header']/a/@href | //div[@class='offer-price']"
xpaths = xpath.split(' | ')

#process.crawl(MySpider)
process.crawl(MySpider, input='inputargument', urls=urls, xpaths=xpaths, last='Bond')
process.start() # the script will block here until the crawling is finished