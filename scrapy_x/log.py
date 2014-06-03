from scrapy import log


class Log(object):

    @staticmethod
    def debug(msg):
        log.msg(msg, loglevel=log.DEBUG)
        return

    @staticmethod
    def info(msg):
        log.msg(msg, loglevel=log.INFO)
        return

    @staticmethod
    def warning(msg):
        log.msg(msg, loglevel=log.WARNING)
        return

    @staticmethod
    def error(msg):
        log.msg(msg, loglevel=log.ERROR)
        return

    @staticmethod
    def critical(msg):
        log.msg(msg, loglevel=log.CRITICAL)
        return
