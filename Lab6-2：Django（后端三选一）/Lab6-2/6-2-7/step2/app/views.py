from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app import models

# Create your views here.
@csrf_exempt
def index(request):
    # ********** Begin ********** #
    dir_ = {}
    if request.method == 'POST':
        username = request.POST.get("username") # 获取username参数
        dir_['datas'] = models.UserInfo.objects.filter(username__contains=username)  # 模糊查询
        dir_['username'] = username  # 传递表单参数
    else:
        dir_['datas'] = models.UserInfo.objects.all()  # GET 查询所有数据
    return render(request, "index.html", dir_)
    # ********** End ********** #