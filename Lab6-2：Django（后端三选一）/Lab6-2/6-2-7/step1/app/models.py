from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # ********** Begin ********** #

    # 用户名：字符串，最大长度20
    username = models.CharField(max_length=20)
    # 性别：字符串，最大长度20
    sex = models.CharField(max_length=20)
    # 签名：字符串，最大长度100
    sign = models.CharField(max_length=100)
    # ********** End ********** #