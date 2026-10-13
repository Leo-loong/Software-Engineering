from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app import models

# Create your views here.
@csrf_exempt
def index(request):
    # ********** Begin ********** #
    dir_ = {}
    if request.method == 'POST':
        # 获取id参数
        uid = request.POST.get('id')
        # 根据id查询并删除数据
        user = models.UserInfo.objects.get(id=uid)
        user.delete()
    dir_['list'] = models.UserInfo.objects.all()
    return render(request, "index.html", dir_)
    # ********** End ********** #