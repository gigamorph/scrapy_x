class Request(object):

    @classmethod
    def is_redirect(cls, request):
        return request.meta.has_key('redirect_times')

    @classmethod
    def get_redirect_urls(cls, request):
        return request.meta.get('redirect_urls', [])

    @classmethod
    def get_orig_url(cls, request):
        redirect_urls = cls.get_redirect_urls(request)
        if len(redirect_urls) > 0:
            return redirect_urls[0]
        else:
            return request.url
