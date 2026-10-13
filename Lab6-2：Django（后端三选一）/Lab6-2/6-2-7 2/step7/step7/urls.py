from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
	# ********** Begin ********** #
    path('index', views.index),
    path('edit/<int:uid>', views.editUsers,name="editusers"),
    path('updateUserInfo', views.updateUserInfo)
    # ********** End ********** #
]
