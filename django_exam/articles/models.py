from django.db import models
# email인지 아닌지 유효성 검사
from django.core.validators import EmailValidator, MinValueValidator
from django.conf import settings

# article.user
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField() # 내용이 길기때문에 textfield
    created_at = models.DateTimeField(auto_now_add=True)
    # datefield가 아니라 datetimefield 로 날짜와 시간을 같이 저장한다.
    # auto_now_add=True 처음 생성될때만

    updated_at = models.DateTimeField(auto_now=True)
    # auto_now=True 정보가 새로워질때마다

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 시험, 다른 곳에선 get_user_model로 호출하지만, models.py에서는 django settings.py에서 직접 가져온다.

    liked_users = models.ManyToManyField(
    settings.AUTH_USER_MODEL,
    related_name='liked_articles', 
    )
    # article.liked_users.all() 아티클을 졸아하는 모든 유저
    # user.liked_articles.all() 유저가 좋아하는 모든 아티클

    class Meta:
        ordering = ['-pk']

# user.??? -> user입장에서 article을 꺼낼때는 comment.article
# article.comment_set.all()
# artocle.comments.all()
class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    # Comment와 User간 1:N 관계
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)

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

