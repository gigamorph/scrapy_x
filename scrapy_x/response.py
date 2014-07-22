import re


class Response(object):

    @classmethod
    def is_html(cls, response):
        headers = response.headers
        if headers.has_key('content-type'):
            content_type_str = response.headers['content-type']
            return re.search(r'text/html', content_type_str) != None
        else:
            return False
