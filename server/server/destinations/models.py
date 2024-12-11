from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    date_created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.name
    

class Preview(models.Model):
    place_name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=500)


class Destination(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    guide = models.TextField()
    image = models.CharField(max_length=255, null=True, blank=True)
    previews_id = models.ManyToManyField(Preview)
    best_time_visit = models.CharField(max_length=100)
    worst_time_visit = models.CharField(max_length=100)
    category_id = models.ManyToManyField(Category)
    date_created = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.name
