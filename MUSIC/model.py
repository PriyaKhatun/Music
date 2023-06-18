from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

class MusicFile(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'
    VISIBILITY_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
        (PROTECTED, 'Protected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='music_files')
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES)

class AccessRequest(models.Model):
    music_file = models.ForeignKey(MusicFile, on_delete=models.CASCADE)
    email = models.EmailField()
