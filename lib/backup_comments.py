# class AppHandlers:
#     def __init__(self):
#         self.get_urls = dict()
#         self.use_hooks = list()
# t1 = lambda a, b: \
#     print(a, b)
#
#
# t1(2, 3)
#
#
# def test(cb):
#     cb()
#
#
# def prnt():
#     print("test")
#
#
# test(lambda: print("test"))

# if self.path in self.get_urls:
#     self.send_response(200)
#     self.send_header("Content-type", "text/html")
#     self.end_headers()
#     # request_self = self
#
#     # class Conn:
#     #     def send(self, data):
#     #         request_self.wfile.write(data)
#     #
#     #     path = request_self.path
#     # get_urls.get(self.path)({"send": self.wfile.write, "path": self.path})
#     self.get_urls.get(self.path)(req)
#
#     # self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
#     # self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
#     # self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
#     # self.wfile.write(bytes("</body></html>", "utf-8"))
# else:
#     self.send_response(200)
#     self.send_header("Content-type", "application/json")
#     # self.send_header("Content-type", "text/html")
#     self.end_headers()
#     self.wfile.write(bytes(json.dumps({"error": "Cannot GET %s" % self.path}), "utf-8"))
#     # self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
#     # self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
#     # self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
#     # self.wfile.write(bytes("</body></html>", "utf-8"))
# hook_count = len(self.app_handlers.use_hooks)
# self.app_handlers.use_hooks.insert(hook_count, cb)
# self.get_urls = app_handlers.get_urls
# self.use_hooks = app_handlers.use_hooks
# for use_hook in self.use_hooks:
#     use_hook(req)