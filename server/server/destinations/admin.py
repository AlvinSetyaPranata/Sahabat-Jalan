from django.contrib import admin
from .models import (
    Destination,
    Category,
    Preview
)

# Register your models here.
admin.site.register(Destination)
admin.site.register(Category)
admin.site.register(Preview)