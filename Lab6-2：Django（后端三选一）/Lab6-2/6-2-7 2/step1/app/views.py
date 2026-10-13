from django.shortcuts import render

from app import models

# Create your views here.
def index(request):
    # ********** Begin ********** #
    users = models.UserInfo.objects.all()
    dir_ = {
        'datas': # your code
    }
    return render(request, "index.html", dir_)
	
    # ********** End ********** #