from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGECHOICE = (
    ("All", "All"),
    ("Kids", "Kids"),
)

MOVIECHOICES = (
    ("seasonal", "Seasonal"),
    ("single", "Single"),
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField("Profile", blank = True)


class Profile(models.Model):
    name = models.CharField(max_length=225)
    ageLimit = models.CharField(max_length=10, choices=AGECHOICE)
    uuid = models.UUIDField(default=uuid.uuid4)

class Movies(models.Model):
    movieTitle = models.CharField(max_length=225)
    movieDescription = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=10, choices=MOVIECHOICES)
    videoFile = models.ManyToManyField("Video")
    moviePoster = models.ImageField(upload_to="poster")
    ageLimit = models.CharField(max_length=10, choices=AGECHOICE)

class Video(models.Model):
    movieName = models.CharField(max_length=225, blank=True, null=True)
    movieFile = models.FileField(upload_to="movie")