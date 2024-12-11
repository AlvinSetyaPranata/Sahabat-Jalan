from rest_framework.serializers import (
    ModelSerializer
)
from .models import (
    Destination,
    Category,
    Preview
)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PreviewSerializer(ModelSerializer):
    class Meta:
        model = Preview
        fields = '__all__'

class DestinationDetailSerializer(ModelSerializer):
    category_id = CategorySerializer(read_only=True, many=True)
    previews_id = PreviewSerializer(read_only=True, many=True)

    class Meta:
        model = Destination
        fields = '__all__'


class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'name', 'location', 'image']