from django.urls import path
from . import views

urlpatterns = [
    path('num_result/', views.num_result),
    path('num/', views.num),

    path('static_example/', views.static_example),

    path('lotto_result/', views.lotto_result),
    path('user_lotto_number/', views.user_lotto_number),

    path('result/', views.result),
    path('search/', views.search),

    path('lotto/', views.lotto),
    path('isitbirthday2/<str:mybd>/', views.isitbirthday2),
    path('isitbirthday/<str:mybd>/', views.isitbirthday),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('greeting/<str:name>/', views.greeting),
    path('image/', views.image),
    path('dinner/<str:name>/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
]