from django.http import HttpResponse
from django.shortcuts import render

class MyMiddleware:
    # ********** Begin ********** #
    def __init__(self, get_response):
        
        self.get_response = get_response

    def __call__(self, request):

        
        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):
        # 异常中间件捕捉其异常并返回一个模板页面（模板页面路径为：index.html）给用户
        return render(request, "index.html")
        
    # ********** End ********** #