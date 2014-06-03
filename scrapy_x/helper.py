## Helpers for Scrapy

import re
import requests

from scrapy import log
from scrapy.exceptions import CloseSpider

def debug(msg):
    log.msg(msg, loglevel=log.DEBUG)
    return

def info(msg):
    log.msg(msg, loglevel=log.INFO)
    return

def warning(msg):
    log.msg(msg, loglevel=log.WARNING)
    return

def error(msg):
    log.msg(msg, loglevel=log.ERROR)
    return

def critical(msg):
    log.msg(msg, loglevel=log.CRITICAL)
    return

def response_is_html(response):
    headers = response.headers
    if headers.has_key('content-type'):
        content_type_str = response.headers['content-type']
        return re.search(r'text/html', content_type_str) != None
    else:
        return False

def request_is_redirect(request):
    return request.meta.has_key('redirect_times')

def request_get_redirect_urls(request):
    return request.meta.get('redirect_urls', [])

def request_get_orig_url(request):
    redirect_urls = request_get_redirect_urls(request)
    if len(redirect_urls) > 0:
        return redirect_urls[0]
    else:
        return request.url

def close_spider(msg):
    raise CloseSpider(msg)
