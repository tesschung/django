from django.urls import path
from . import views

# namespace를 정의 한다. 
app_name = 'accounts'

# urlpatterns가 있어야 error가 발생하지 않는다
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete')
]


