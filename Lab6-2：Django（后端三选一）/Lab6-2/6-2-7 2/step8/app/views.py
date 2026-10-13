from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app import models
from django.shortcuts import redirect


# 用户列表
@csrf_exempt
def index(request):
    # ********** Begin ********** #


    # ********** End ********** #
	
	
# 加载修改表单信息
@csrf_exempt
def editUser(request, id):
    # ********** Begin ********** #


    # ********** End ********** #
	
	
# 修改用户信息
@csrf_exempt
def updateUserInfo(request):
    # ********** Begin ********** #


    # ********** End ********** #
	
	
# 删除用户
@csrf_exempt
def deleteUser(request, id):
    # ********** Begin ********** #


    # ********** End ********** #
	
	
# 新增用户
@csrf_exempt
def addUserInfo(request):
    # ********** Begin ********** #


    # ********** End ********** #
	
	
# 加载新增用户表单
@csrf_exempt
def addUserInfoPage(request):
    # ********** Begin ********** #
 
 
    # ********** End ********** #