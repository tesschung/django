from django.db import models

# Create your models here.

# article입장에서 comment를 바로 가져올 수 없기때문에 따로 불러와야 한다.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # on_delete=models.CASCADE == 'Article이 삭제되면 Comment도 함께 삭제'
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 자동으로 데이터를 꺼낼때 역순으로 가져올 수 있도록 함. 즉 마지막에 생성된 댓글부터 조회
    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content
    