from django.db import models
# Create your models here.
class BookInfo(models.Model):
    # ********** Begin ********** #
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    # ********** End ********** #
	
class HeroInfo(models.Model):
    # ********** Begin ********** #
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=20)
    # 一对多外键关联 BookInfo，Django2.0+ 必须指定 on_delete
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    # ********** End ********** #