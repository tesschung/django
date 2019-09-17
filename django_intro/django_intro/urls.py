"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django_intro/urls.py
from django.contrib import admin
from django.urls import path, include # include는 다른 urls를 참조 할 수 있도록 한다.
# from pages import views # pages라는 application에서 views를 import한다.

# www.ssafy.com/login => 아래에 정의가 되어있지 않아서 404 not found
# www.ssafy.com/index => views.index
urlpatterns = [
    # path('사용자가 접속하는 경로')
    # pages에 있는 urls.py로 가도록 설정
    path('utilities/', include('utilities.urls')),
    path('pages/', include('pages.urls')), 
    path('admin/', admin.site.urls),
]
