from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
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

    @extend_schema(responses={
        200: DestinationSerializer
    }, request=DestinationSerializer)


    def get(self, _):
        serializer = DestinationSerializer(Destination.objects.all(), many=True)

        return Response(serializer.data)



class CategoryView(APIView):

    @extend_schema(responses={
        200: CategorySerializer
    }, request=CategorySerializer)
    def get(self, _):
        serializer = CategorySerializer(Category.objects.all(), many=True)

        return Response(serializer.data)



