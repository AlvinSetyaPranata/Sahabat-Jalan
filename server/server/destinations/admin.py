from django.contrib import admin
from .models import (
    Destination,
    Category
)

# Register your models here.
admin.site.register(Destination)
admin.site.register(Category)