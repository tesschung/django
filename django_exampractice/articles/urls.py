from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 모든 게시글이 보일 페이지
    path('', views.index, name='index'),
    # 게시글을 만드는 페이지
    path('create/', views.create, name='create'),

    path('<int:article_pk>/delete/', views.delete, name='delete'),
    
    # 게시글의 상세 페이지
    path('<int:article_pk>/', views.detail, name='detail'),

    # articles/3/comment_create/
    path('<int:article_pk>/comment_create/', views.comment_create, name='comment_create'),

    path('<int:comment_pk>/<int:article_pk>/', views.comment_delete, name='comment_delete'),
]
