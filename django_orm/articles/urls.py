from django.urls import path
from . import views

#articles/___ 이후의 경로
urlpatterns = [
    path('create/', views.create),
    path('new/', views.new),
    path('index/', views.index),
]
