from django.http import HttpResponseForbidden,HttpResponse


class BlackListMiddleware():
    BLACKLIST = [
        'Python3.6'
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ********** Begin ********** #
        agent = request.META.get('HTTP_USER_AGENT', None)
        
        if agent in self.BLACKLIST:
            return HttpResponseForbidden('<h1>该IP地址被限制访问！请在24小时后进行访问</h1>')
        response = self.get_response(request)
        
        # ********** End ********** #