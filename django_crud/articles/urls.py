from django.urls import path
from . import views # 같은 파일내 views.py의 함수를 불러온다.
# 사용자는 /articles/ ___ 인 상태
urlpatterns = [
    path('', views.index),
    # 사용자에게 상세페이지 제공
    path('detail/<int:article_pk>/', views.detail),
    # 사용자에게 입력 페이지 제공
    path('new/', views.new), # 이와같이 view.new 함수를 호출
    # 데이터를 전달받아서 article 생성
    path('create/', views.create),
    # 삭제
    path('<int:article_pk>/delete/', views.delete),
]
