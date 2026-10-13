from django.urls import path, re_path

from testapp import views
urlpatterns = [

#********** Begin **********#

    re_path(r'^test/(?P<n>\d+)/$', views.index),
#********** End **********#

]