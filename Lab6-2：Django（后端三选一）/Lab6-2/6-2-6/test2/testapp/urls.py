from django.urls import path

from testapp import views, views3, views4, views5




urlpatterns = [
    path("", views.index),
    path('method_show/', views.method_show),
    path('', views.index),
    path('your-name/', views.search),
    path('sub/', views.sub),
    path('sea/', views3.sea),
    path('index3/',views.index3),
    path('search/', views3.search),
    path('index2/', views3.index2),
    path('get_cookie/', views4.get_cookie),
    path('set_session/', views4.set_session),
    path('session_test/', views5.session_test),
    path('session_test1/', views5.session_test1),
    path('session_test2/', views5.session_test2),
    path('cookie_set/', views5.cookie_set),
]


