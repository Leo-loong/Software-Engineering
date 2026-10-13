from django.http import HttpResponse


def get_cookie(request):

    response = HttpResponse("读取Cookie，数据如下：<br>")
    # ********** Begin **********#
    # 获取名为 name 的 Cookie 值
    name_cookie = request.COOKIES.get('name', '')
    # 使用 <h1> 标签展示 Cookie 内容
    response.write(f"<h1>{name_cookie}</h1>")
    # ********** End **********#
    return response

def set_session(request):
    # ********** Begin **********#
    # 向 session 中存入键 hw，值为 hello world
    request.session['hw'] = 'hello world'
    # ********** End **********#
    return HttpResponse('写session')