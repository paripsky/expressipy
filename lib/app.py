from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import json
from lib.log import Log


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass


class Request:
    def __init__(self, request_self):
        self.request_self = request_self
        self.path = request_self.path

    def send(self, data):
        self.request_self.wfile.write(data)


class App:
    hostName = "localhost"
    hostPort = 9000

    def __init__(self):
        self.app_handlers = list()

    class MyServer(BaseHTTPRequestHandler):
        def __init__(self, app_handlers, *args):
            self.app_handlers = app_handlers
            BaseHTTPRequestHandler.__init__(self, *args)

        @staticmethod
        def matches_handler_path(url, handler_path):
            # TODO: include pattern matching
            return url == handler_path

        def do_GET(self):
            req = Request(self)

            # TODO: find a way to skip iterating non matching handlers, but keep the handler order
            matching_handlers_found = False
            for app_handler in self.app_handlers:
                handler_url = app_handler[0]
                handler = app_handler[1]
                if handler_url == "*":
                    handler(req)
                elif self.matches_handler_path(self.path, handler_url):
                    matching_handlers_found = True
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    # handler(req, next)
                    handler(req)

            # if no matching handlers were found, respond with 404
            if not matching_handlers_found:
                self.send_response(404)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                error = {"statusCode": 404, "error": "Cannot GET %s" % self.path}
                self.wfile.write(bytes(json.dumps(error), "utf-8"))

        def do_POST(self):
            pass

    def listen(self, port):
        def serve(self):
            try:
                def handler(*args):
                    self.MyServer(self.app_handlers, *args)

                my_server = ThreadingHTTPServer((self.hostName, port), handler)
            except OSError:
                print("port %s is already in use" % port)
            Log.info("Server Started - %s:%s" % (self.hostName, port))

            try:
                my_server.serve_forever()
            except KeyboardInterrupt:
                pass

            my_server.server_close()
            Log.info("Server Stopped - %s:%s" % (self.hostName, port))

        Thread(target=serve, args=[self]).start()
    # FIXME: separate get and post handlers?
    def get(self, url, cb):
        self.app_handlers.append((url, cb))

    def use(self, cb):
        self.app_handlers.append(("*", cb))
