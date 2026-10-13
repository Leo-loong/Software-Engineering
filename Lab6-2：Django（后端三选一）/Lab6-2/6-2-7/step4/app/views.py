from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app import models

# Create your views here.
@csrf_exempt
def index(request):
    # ********** Begin ********** #
    dir_ = {}
    if request.method == 'POST':
        btitle_ = request.POST.get("btitle") # 获取btitle参数
        # 根据图书名称反向查询对应所有英雄
        dir_['list'] = models.HeroInfo.objects.filter(hbook__btitle=btitle_)
    # 查询所有图书信息
    dir_['bookList'] = models.BookInfo.objects.all()
    return render(request, "index.html", dir_)
    # ********** End ********** #