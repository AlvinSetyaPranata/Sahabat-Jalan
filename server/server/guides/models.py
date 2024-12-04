from django.db import models

# Create your models here.
class Guide(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    date_created = models.DateTimeField(editable=False, auto_now_add=True)