from django.urls import path 
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# get_schema_view로 전달 받음
schema_view = get_schema_view(
    openapi.Info(
        title='Music API',
        default_version='v1',
        description='음악 관련 API 서비스입니다.',
        terms_of_service='https://www.google.com/policies/terms/',
    )
)

app_name = 'musics'
# /api/v1/
urlpatterns = [
    path('musics/', views.music_list, name='music_list'), 
    path('musics/<int:music_pk>/', views.music_detail, name='music_detail'),
    path('artists/', views.artist_list, name='artist_list'), 
    path('artists/<int:artist_pk>/', views.artist_detail, name='artist_detail'),
    path('comments/', views.comment_list, name='comment_list'), 
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'), # ui가 있는 상태에서 진행
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger')
]

