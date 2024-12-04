from django.shortcuts import render
from rest_framework.viewsets import (
    ModelViewSet
)
from .serializers import GuideSerializer
from .models import Guide

# Create your views here.

class DestinationView(ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
