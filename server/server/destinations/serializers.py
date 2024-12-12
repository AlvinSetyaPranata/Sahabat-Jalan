from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    CharField
)
from .models import (
    Destination,
    Category,
)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DestinationDetailSerializer(ModelSerializer):
    category_id = CategorySerializer(read_only=True, many=True)
    previews = ListField(child=CharField())

    class Meta:
        model = Destination
        fields = '__all__'


class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'name', 'location', 'image']


class SearchSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'name', 'rating']