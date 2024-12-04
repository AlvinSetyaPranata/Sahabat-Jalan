from rest_framework.serializers import ModelSerializer
from .models import Destination

class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'