from scrapy.exceptions import CloseSpider

class Spider(object):

    @classmethod
    def close(cls, msg='scrapy_x.Spider.close'):
        raise CloseSpider(msg)
