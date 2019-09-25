from django.urls import path
from . import views # 같은 파일내 views.py의 함수를 불러온다.

app_name = 'articles'
# 사용자는 /articles/ ___ 인 상태
urlpatterns = [
    path('', views.index, name='index'),
    # 사용자에게 입력 페이지 제공
    # path('new/', views.new, name='new'), # 이와같이 view.new 함수를 호출
    # 데이터를 전달받아서 article 생성
    path('create/', views.create, name='create'),
    # 사용자에게 상세페이지 제공
    path('detail/<int:article_pk>/', views.detail, name='detail'),
    # 삭제
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    
    # 댓글 추가
    path('<int:article_pk>/comments', views.comments_create, name='comments_create'),
    # 댓글 삭제
    # /articles/3/comments/2/delete     article의 3번에 해당하는 comments중에 2에 해당하는 것을 삭제
    path('<int:article_pk>/comments/<int:comment_pk>', views.comments_delete, name='comments_delete'),
]
