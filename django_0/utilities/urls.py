from django.urls import path
from . import views # .은 같은 directory를 뜻한다.

# /utilities/(urlpatterns)
urlpatterns = [
    path('index/', views.index),
]