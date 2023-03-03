from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your tests here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    

