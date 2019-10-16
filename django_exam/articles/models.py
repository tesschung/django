from django.db import models
# email인지 아닌지 유효성 검사
from django.core.validators import EmailValidator, MinValueValidator

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField() # 내용이 길기때문에 textfield
    created_at = models.DateTimeField(auto_now_add=True)
    # datefield가 아니라 datetimefield 로 날짜와 시간을 같이 저장한다.
    # auto_now_add=True 처음 생성될때만

    updated_at = models.DateTimeField(auto_now=True)
    # auto_now=True 정보가 새로워질때마다
    class Meta:
        ordering = ['-pk']


class Person(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(
    max_length=100,
    validators=[EmailValidator(message='이메일 형식에 맞지 않습니다.')]
    )
    age = models.IntegerField(
    validators=[MinValueValidator(19, message='미성년자는 노노')]
    )

