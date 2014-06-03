from scrapy.exceptions import CloseSpider

class Spider(object):

    def close(msg):
        raise CloseSpider(msg)
