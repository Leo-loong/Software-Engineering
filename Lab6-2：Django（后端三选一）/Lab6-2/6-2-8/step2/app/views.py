from django.shortcuts import render

# Create your views here.
def index(request):
    raise Exception('自定义异常')
    return render(request, 'index.html')