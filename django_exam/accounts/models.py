from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    # 모든 유저는 followers을 가지고 있다.
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")



