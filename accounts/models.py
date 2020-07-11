from django.db import models
from django.contrib.auth.models import User
from .enums import UserStatus


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=1, choices=[(s.name, s.value) for s in UserStatus], null=True)

    def __str__(self):
        return f'{self.user}'

