from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:articles_pk>/', views.detail, name='detail'),
    path('<int:articles_pk>/update/', views.update, name='update'), 
    path('<int:articles_pk>/delete/', views.delete, name='delete'),
    path('<int:articles_pk>/like/', views.like, name='like'),
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
