from django.db import models

# 1:N의 관계를 생성한다
# Article에 여러 Comment가 달릴 수 있도록 설정

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
    
class Comment(models.Model):
    # CASCADE article이 지워지면, comment도 같이 지워지도록 한다.
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-pk']

