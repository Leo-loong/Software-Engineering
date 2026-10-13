from django.http import HttpResponse
from testapp.views4 import set_session

def cookie_set(request):
    response = HttpResponse("")
    #三个参数：参数一：cookie名称  参数二：cookie内容  参数三：cookie过期时间
    response.set_cookie('name', 'hello')
    return response

def session_test(request):
    h1=request.session.get('hw')
    if(h1==None):
        return HttpResponse("<h1>设值session失败</h1>")
    return HttpResponse("<h1>hw=%s</h1>" %h1)


def session_test1(request):
    if 'name' in request.COOKIES:
        return HttpResponse("<h1>删除cookie失败</h1>")
    else:
        return HttpResponse("<h1>删除cookie成功</h1>")
        
def session_test2(request):
    set_session(request)
    h1 = request.session.get('hw')
    if (h1 == None):
        return HttpResponse("<h1>设值session失败</h1>")
    return HttpResponse("<h1>hw=%s</h1>" % h1)