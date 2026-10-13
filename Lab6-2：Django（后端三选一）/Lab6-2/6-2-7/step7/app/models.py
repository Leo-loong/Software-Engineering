from django.db import models
# Create your models here.
class UserInfo(models.Model):
    # ********** Begin ********** #
    username = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    sign = models.CharField(max_length=100)
    # ********** End ********** #