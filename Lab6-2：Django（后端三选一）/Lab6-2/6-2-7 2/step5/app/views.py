from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app import models

# Create your views here.
@csrf_exempt
def index(request):
    # ********** Begin ********** #
    dir_ = {}
    if request.method == 'POST':
        # 获取表单参数
        username = request.POST.get('username')
        sex = request.POST.get('sex')
        sign = request.POST.get('sign')
        
        # 创建并保存用户数据
        user = models.UserInfo(
            username=username,
            sex=sex,
            sign=sign
        )
        user.save()

    # 查询所有用户
    list = models.UserInfo.objects.all()
    dir_['list'] = list
    return render(request, "index.html",dir_)
    # ********** End ********** #