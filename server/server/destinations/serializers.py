from rest_framework.serializers import (
    ModelSerializer
)
from .models import (
    Destination,
    Category
)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DestinationDetailSerializer(ModelSerializer):
    category_id = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Destination
        fields = '__all__'


class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = ['name', 'location', 'image']