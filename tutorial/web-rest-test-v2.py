import web
import json
import sctest

urls = (
    '/', 'index'
)

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

class index:
    def GET(self):
		pyDict = {'one':1,'two':2}
		web.header('Content-Type', 'application/json')
		
		process = sctest.CrawlerProcess({
			'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
		})

		#dane wejsciowe:
		urls = [
			"http://allegro.pl/6-i-2002-2008-147321?a_text_i%5B14%5D%5B0%5D=140&a_enum%5B16%5D%5B1%5D=1&a_enum%5B16%5D%5B4%5D=4&a_enum%5B13%5D%5B3%5D=3&price_to=12000&a_text_i%5B4%5D%5B1%5D=190000&a_enum%5B128790%5D%5B2%5D=2&a_enum%5B178%5D%5B1%5D=1",
		]
		xpath = "//h2[@class='offer-header']/a | //h2[@class='offer-header']/a/@href | //div[@class='offer-price']"
		xpaths = xpath.split(' | ')


		
		return json.dumps(pyDict)

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=8888)