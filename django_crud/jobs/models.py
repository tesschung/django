from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=20)
    past_job = models.TextField()
    profile_image = models.ImageField(blank=True)

    # job의 데이터 표현 설정
    def __str__(self):
        return self.name
    
