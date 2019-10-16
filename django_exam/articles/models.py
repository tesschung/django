from django.db import models

# Create your models here.

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



