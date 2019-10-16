from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:articles_pk>/', views.detail, name='detail'),
    path('<int:articles_pk>/update/', views.update, name='update'), 
    path('<int:articles_pk>/delete/', views.delete, name='delete'),
]
