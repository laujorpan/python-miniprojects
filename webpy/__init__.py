import web

urls = (
    '/','Index'
)


class Index:
    def GET(self):
        return "Hello. This is a web.py test"


if __name__  == "__main__":
    app = web.application(urls,globals())
    app.run()