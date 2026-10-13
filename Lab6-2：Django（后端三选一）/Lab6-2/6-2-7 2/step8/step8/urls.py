from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    # ********** Begin ********** #
    path('admin', admin.site.urls),
  
    # ********** End ********** #
]