from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

# artist.musics
class Music(models.Model):
    # Artist와 1:N 관계 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics')
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    # Music과 1:N 관계
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    def __str__(self):
        return f'{self.music.pk}번 음악의 {self.pk}번 댓글'
