import tornado.ioloop
import tornado.web
import random

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Привет мир!")

class ContactsHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("contacts.html")
        #self.write('<h3 class="jumbotron" style="font-size: 40pt; background-color: #FFFFFF;"  > <img src="photos/treasure_chest.jpg" width="10%"/> КЛАДОВЕД </h3>')
        #self.write("<h2 style='align: center; color: blue;'>Привет!</h1>")
class AboutHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("about.html")
class ShopHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("shop.html")
class FeedbackHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("feedback.html")



class PaigeHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("index.html")

class RockHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("rock.html")
class PillowHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("pillow.html")
class plushyFrogsHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("plushy_frogs.html")
class JhabaDrHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("jhaba_dr.html")
class JhabuddaHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("jhabudda.html")
class CustomizableMagnetHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("customizable_magnet.html")
class print_jhabaHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("print_jhaba.html")
class HugsHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("hugs.html")
class PebbleHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("pebble.html")
class EliseDHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("elise_d.html")
class PrintsHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("prints.html")
class CustomizableThingsHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("customizable_things.html")
class ZlayazebbaHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("zlayazebba.html")
class AngryToadHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("angry_toad.html")
settings = [
    ('/', MainHandler),
    ('/about.html', AboutHandler),
    ('/index.html', PaigeHandler),
    ('/shop.html', ShopHandler),
    ('/contacts.html', ContactsHandler),
    ('/feedback.html', FeedbackHandler),
    ('/rock.html', RockHandler),
    ('/print_jhaba.html', print_jhabaHandler),
    ('/jhabudda.html', JhabuddaHandler),
    ('/pillow.html', PillowHandler),
    ('/plushy_frogs.html', plushyFrogsHandler),
    ('/jhaba_dr.html', JhabaDrHandler),
    ('/hugs.html', HugsHandler),
    ('/pebble.html', PebbleHandler),
    ('/elise_d.html', EliseDHandler),
    ('/zlayazebba.html', ZlayazebbaHandler),
    ('/angry_toad.html', AngryToadHandler),
    ('/prints.html', PrintsHandler),
    ('/customizable_things.html', CustomizableThingsHandler),

    ('/customizable_magnet.html', CustomizableMagnetHandler),


    ('/photos/(.*)', tornado.web.StaticFileHandler, {'path': 'photos'}),
]

app = tornado.web.Application(settings)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()