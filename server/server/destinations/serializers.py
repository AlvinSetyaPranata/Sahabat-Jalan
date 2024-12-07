from rest_framework.serializers import ModelSerializer
from .models import (
    Destination,
    Category
)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DestinationSerializer(ModelSerializer):
    category_id = CategorySerializer()

    class Meta:
        model = Destination
        fields = '__all__'