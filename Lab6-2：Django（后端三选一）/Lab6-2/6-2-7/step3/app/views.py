from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app import models

# Create your views here.
@csrf_exempt
def index(request):
    # ********** Begin ********** #
    dir_={}
    dir_['datas'] = models.UserInfo.objects.all()  # 所有用户信息
    dir_['count'] = models.UserInfo.objects.count()  # 用户人数
    dir_['malecount'] = models.UserInfo.objects.filter(sex='男').count()  # 性别为男的用户人数
    dir_['femalecount'] = models.UserInfo.objects.filter(sex='女').count()  # 性别为女的用户人数
    return render(request, "index.html", dir_)
    # ********** End ********** #