## Helpers for Scrapy

import re
import requests


from scrapy.exceptions import CloseSpider


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
