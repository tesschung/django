from django.urls import path
from . import views

# domain.com/articles/ ____
urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    # /articles/1/delete/
    path('<int:article_pk>/delete/', views.delete),
    # /articles/8/edit/
    path('<int:article_pk>/edit/', views.edit),
    path('<int:article_pk>/update/', views.update),
]
