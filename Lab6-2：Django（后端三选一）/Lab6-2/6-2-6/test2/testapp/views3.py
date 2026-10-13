
from django.http import HttpResponse
from django.shortcuts import render, redirect


#以下是HttpResponse练习

def sea(request):
    return render(request, "testapp/search.html", )



def search(request):
    # ********** Begin **********#
    
    your_name = request.GET.get('your_name', '')
    # 判断是否为空，空则重定向到index2
    if not your_name:
        return redirect('index2')
    
    # ********** End **********#
    return HttpResponse("<html><body><h1>your_name=%s</h1> </body></html>" %your_name)





def index2(request):
    return HttpResponse("<html><body><h1>没有输入东西</h1></body></html>")

