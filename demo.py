from lib.app import App

app = App()

app2 = App()

count = 0


def tst(req):
    # print(req["user"])
    global count
    count += 1
    req.user = "user1"
    req.send(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
    req.send(bytes("<body><p>This is test no %d.</p>" % count, "utf-8"))
    req.send(bytes("<p>You accessed path: %s</p>" % req.path, "utf-8"))
    req.send(bytes("</body></html>", "utf-8"))
    print(req.user)


def logger(req):
    print("logging middleware is here.")


app.use(logger)

app.get("/demo", tst)

app.listen(9000)

app2.get("/demo2", tst)

app2.listen(9001)
