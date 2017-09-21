#
# Created by Cooper on 2017/6/6.
#

import base64, re
import numpy as np
import scipy as sp
import time
from scipy import misc
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from tornado import web, ioloop, gen
from tornado.concurrent import run_on_executor
import os, io
from classifiers.classifier import predict

types = [x for x in os.listdir(os.path.dirname(__file__) + "/classifiers") if x[:4] == "type"]


class MainHandler(web.RequestHandler):
    def get(self):
        self.render("index.html", title="home")


class AboutHandler(web.RequestHandler):
    def get(self):
        self.render("about.html", title="about")


class ReleaseHandler(web.RequestHandler):
    def get(self):
        self.render("release.html", title="release")


class TestHandler(web.RequestHandler):
    def get(self):
        self.render("test.html", title="test", types=types, img_base64="", pred="")

    def post(self):
        type = self.get_argument('type')
        img_file = self.request.files['img'][0]
        img_base64 = 'data:image/jpg;base64,' + base64.b64encode(img_file.body).decode('utf-8')
        pred = predict(type, img_base64)
        self.render('test.html', title="test", types=types, img_base64=img_base64, pred=pred)


class PredictHandler(web.RequestHandler):
    def post(self):
        type = self.get_argument('type')
        img_base64 = self.get_argument('img_base64')
        pred = predict(type, img_base64)
        self.finish({"predict": pred, "result": "ok"})


app = web.Application([
    (r"/", MainHandler),
    (r"/test", TestHandler),
    (r"/about", AboutHandler),
    (r"/release", ReleaseHandler),
    (r"/predict", PredictHandler),
    (r"/classifiers/(.*)", web.StaticFileHandler, {'path': r"./classifiers"}),
], template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static")
)

if __name__ == '__main__':
    app.listen(8885)
    ioloop.IOLoop.instance().start()
