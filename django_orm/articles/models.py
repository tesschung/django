from django.db import models

# Create your models here.
# table을 class처럼

class Article(models.Model): # django Model을 상속 받는다.
# id(pk)는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
# database는 primary key PK 가 반드시 있어야 한다.
    # id = models.AutoField(primary_key=True)

    # CharField에서는 max_length가 필수 인자다.
    title = models.CharField(max_length=20) # 클래스 변수 (DB 필드)
    content = models.TextField() # 클래스 변수 (DB 필드)
    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 지금 추가되었을때