from django.urls import path
from . import views # 같은 파일내 views.py의 함수를 불러온다.


app_name = 'jobs'
urlpatterns = [
    # 처음에 사용자가 바로 접근해서 입력하는 페이지
    # 사용자의 입력을 받는 페이지
    path('', views.index, name='index'),
    path('<int:job_pk>/past_job/', views.past_job, name='past_job'),
]