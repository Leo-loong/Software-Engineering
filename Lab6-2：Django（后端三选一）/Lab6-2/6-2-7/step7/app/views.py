from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app import models
from django.shortcuts import redirect

# Create your views here.
@csrf_exempt
def index(request):
    dir_ = {}
    list = models.UserInfo.objects.all()
    dir_['list'] = list
    return render(request, "index.html", dir_)

@csrf_exempt
def editUsers(request, uid):
    u = models.UserInfo.objects.get(id=uid)
    return render(request, "edit.html", {"data": u})

@csrf_exempt
def updateUserInfo(request):
    # ********** Begin ********** #
    # 获取参数
    id = request.POST.get('id')
    username = request.POST.get('username')
    sign = request.POST.get('sign')
    
    # 查询用户并修改
    user = models.UserInfo.objects.get(id=id)
    user.username = username
    user.sign = sign
    user.save()
    
    # ********** End ********** #
    return redirect("/index")