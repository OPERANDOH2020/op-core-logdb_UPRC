 # Copyright (c) 2016 {UPRC}.
 # All rights reserved. This program and the accompanying materials
 # are made available under the terms of the The MIT License (MIT).
 # which accompanies this distribution, and is available at
 # http://opensource.org/licenses/MIT

 # Contributors:
 #    {Constantinos Patsakis} {UPRC}
 # Initially developed in the context of OPERANDO EU project www.operando.eu

from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.httpserver
import bson
import pymongo
from time import time
import hmac

# read password
passfile = open("passfile.key", "r")
passwd = passfile.read()

H = hmac.new(passwd)

conn = pymongo.MongoClient()
db = conn.logdb

current_milli_time = lambda: int(time() * 1000)


def strfy(L):
    lst = [str(i) for i in L]
    return "".join(lst)


class LogEvent(tornado.web.RequestHandler):

    def post(self):
        data = strfy(
            [current_milli_time(
            ), self.get_argument(
                "RequestID"), self.get_argument("RequestingComponent"), self.get_argument("IP"), self.get_argument("mac"), self.get_argument("RequestedURL"),
                self.get_argument("RequestedData"), self.get_argument("Action"), self.get_argument("ClientTypeID"), self.get_argument("UserID", ''), self.get_argument("ServiceID", ''), self.get_argument("ProxyID", '')])
        H.update(data)
        event = {
            'TS':  current_milli_time(),
            'RID': self.get_argument("RequestID"),
            'RC': self.get_argument("RequestingComponent"),
            'IP': self.get_argument("IP"),
            'mac': self.get_argument("mac"),
            'url': self.get_argument("RequestedURL"),
            'data': self.get_argument("RequestedData"),
            'action': self.get_argument("Action"),
            'client': self.get_argument("ClientTypeID"),
            'user': self.get_argument("UserID", ''),
            'service': self.get_argument("ServiceID", ''),
            'proxy': self.get_argument("ProxyID", ''),
            'H': H.hexdigest()
        }

        try:
            db.events.insert(event, w=1)
            te = time()
            self.write("1")
        except:
            self.write("0")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/log", LogEvent)
    ])
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)

    server.start(0)
    tornado.ioloop.IOLoop.instance().start()
