from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class User(AbstractBaseUser):
    name = models.EmailField(verbose_name="Email", unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)