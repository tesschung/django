from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField

# article입장에서 comment를 바로 가져올 수 없기때문에 따로 불러와야 한다.
class Article(models.Model): # article에 img 저장
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True) # 문자열 빈 값 저장은 null값이 아니라 ''(빈스트링)
    sub_content = models.IntegerField(null=True) # 문자열을 제외하고는 ''(빈스트링), Null(null값) 두 가지 가능
    # blank: 데이터 유효성과 관련되어있다.
    # null: DB와 관련되어있다.
    # ''(빈스트링), Null(null값) 두 가지로 저장결과가 달라진다.
    image = models.ImageField(blank=True) # 데이터가 들어오기 전에 blank값이 들어와도 저장할 수 있도록 기본 설정
    # image 필드에서 부터 가지고 올 것
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality':90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # on_delete=models.CASCADE == 'Article이 삭제되면 Comment도 함께 삭제'
    # related_name은 원래 article.comment_set으로 썼던 것을 article.comments로 쓸 수 있도록 변경
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 자동으로 데이터를 꺼낼때 역순으로 가져올 수 있도록 함. 즉 마지막에 생성된 댓글부터 조회
    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content

class School(models.Model):
    school_name = models.CharField(max_length=20)

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

class Question(models.Model):
    question = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50)

class Comment_question(models.Model):
    comment_question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Choice(models.Model):
    content = models.CharField(max_length=50)
    votes = models.IntegerField(null=True)
    class Meta:
        ordering = ['-pk']
​
    def __str__(self):
        return self.content