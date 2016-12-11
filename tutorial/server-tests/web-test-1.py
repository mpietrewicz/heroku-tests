import web
import json

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
		
		return json.dumps(pyDict)

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=8080)