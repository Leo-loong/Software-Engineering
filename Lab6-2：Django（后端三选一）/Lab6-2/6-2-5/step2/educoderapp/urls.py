from django.urls import path
from educoderapp import views
urlpatterns = [
    # ********** Begin ********** #
     path('', views.hello),
    # ********** End ********** #
]