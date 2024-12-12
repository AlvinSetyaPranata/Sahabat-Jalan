from django.contrib import admin
from .models import (
    Destination,
    Category
)
from .forms import DestinationForm

class DestinationAdmin(admin.ModelAdmin):
    form = DestinationForm

# Register your models here.
admin.site.register(Category)
admin.site.register(Destination, DestinationAdmin)