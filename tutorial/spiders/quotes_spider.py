import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.olx.pl/oferty/q-raspberry/',
            'http://allegro.pl/6-i-2002-2008-147321?a_text_i%5B14%5D%5B0%5D=140&a_enum%5B16%5D%5B1%5D=1&a_enum%5B16%5D%5B4%5D=4&a_enum%5B13%5D%5B3%5D=3&price_to=12000&a_text_i%5B4%5D%5B1%5D=190000&a_enum%5B128790%5D%5B2%5D=2&a_enum%5B178%5D%5B1%5D=1',
			'http://suchen.mobile.de/fahrzeuge/auto?isSearchRequest=true&vc=Car&dam=0&ms=1100%3B',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)