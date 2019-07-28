import time


class Log:
    @staticmethod
    def info(message):
        print("%s - %s\n" % (time.asctime(), message))
