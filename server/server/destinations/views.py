from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Destination,
    Category
)
from .serializers import (
    DestinationSerializer,
    CategorySerializer
)


# Create your views here.
class DestinationView(APIView):

    def get(self, _):
        serializer = DestinationSerializer(Destination.objects.all(), many=True)

        return Response(serializer.data)



class CategoryView(APIView):
    def get(self, _):
        serializer = CategorySerializer(Category.objects.all(), many=True)

        return Response(serializer.data)


