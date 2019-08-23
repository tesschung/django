from django.db import models

# Create your models here.
# table을 class처럼

#1. 작성: model 작성
#2. 알림: python manage.py makemigrations => django 한테 model 작성했음을 알림
#3. 명령: python manage.py migrate => django 한테 실제 DB에 작성하라고 명령


class Article(models.Model): # django Model을 상속 받는다.
    # id(pk)는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    # database는 primary key PK 가 반드시 있어야 한다.
    # id = models.AutoField(primary_key=True)

    # 모든 필드는 기본적으로 NOT NULL -> 비어있으면 안된다.

    # CharField에서는 max_length가 필수 인자다.
    title = models.CharField(max_length=20) # 클래스 변수 (DB 필드)
    content = models.TextField() # 클래스 변수 (DB 필드)
    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 지금 추가되었을때
    updated_at = models.DateTimeField(auto_now=True) # 수정이 가해질때 해당 시간을 추가

    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    birthday = models.DateField()
    age = models.IntegerField()