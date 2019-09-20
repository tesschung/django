from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # articles 로 들어왔다면 articles/urls.py로 이동
    path('jobs/', include('jobs.urls')),
    path('articles/', include('articles.urls')), 
    path('admin/', admin.site.urls),
]
