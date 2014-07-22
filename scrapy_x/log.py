from scrapy import log


class Log(object):
    
    DEBUG = log.DEBUG
    INFO = log.INFO
    WARNING = log.WARNING
    ERROR = log.ERROR
    CRITICAL = log.CRITICAL
    
    @classmethod
    def start(cls, logfile=None, loglevel=log.DEBUG):
        log.start(logfile=logfile, loglevel=loglevel)

    @classmethod
    def debug(cls, msg):
        log.msg(msg, loglevel=log.DEBUG)
        return

    @classmethod
    def info(cls, msg):
        log.msg(msg, loglevel=log.INFO)
        return

    @classmethod
    def warning(cls, msg):
        log.msg(msg, loglevel=log.WARNING)
        return

    @classmethod
    def error(cls, msg):
        log.msg(msg, loglevel=log.ERROR)
        return

    @classmethod
    def critical(cls, msg):
        log.msg(msg, loglevel=log.CRITICAL)
        return
