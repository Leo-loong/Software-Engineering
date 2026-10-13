from django.shortcuts import render

# Create your views here.


def index(request):
    # ********** Begin **********#
    str=(request.path)
    return render(request, 'testapp/index.html', {'str':str})
    # ********** End **********#

def method_show(request):
    return HttpResponse(request.method)

def sub(request):

    # ********** Begin **********#


	return render(request, 'testapp/detail.html', request.GET)
    # ********** End **********#
