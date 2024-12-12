from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=128, null=True, blank=True)
    google_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    is_google_user = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
