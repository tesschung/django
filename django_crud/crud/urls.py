from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
'''
from django.conf.urls.static import static : 정적 파일을 제공하기 위한 내장함수
from django.conf import settings : settings.py 내 설정한 미디어 경로를 사용할 수 있게 함
'''

urlpatterns = [
    # articles 로 들어왔다면 articles/urls.py로 이동
    path('jobs/', include('jobs.urls')),
    path('articles/', include('articles.urls')), 
    path('admin/', admin.site.urls),
]

#미디어 파일을 주소로 설정하는 코드 작성
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)