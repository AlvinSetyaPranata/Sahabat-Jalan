from django.db import models
from guides.models import (
    Guide
)
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    date_created = models.DateTimeField(editable=False, auto_now_add=True)


class Destination(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    category_id = models.ManyToManyField(Category)
    guide_id = models.OneToOneField(Guide, on_delete=models.CASCADE)
    date_created = models.DateTimeField(editable=False, auto_now_add=True)