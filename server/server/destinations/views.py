from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST
)
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import (
    Destination,
    Category
)
from .serializers import (
    DestinationSerializer,
    DestinationDetailSerializer,
    CategorySerializer,
    SearchSerializer
)


# Create your views here.
class DestinationView(APIView):

    @extend_schema(responses={
        200: DestinationSerializer
    }, request=DestinationSerializer)


    def get(self, _):
        serializer = DestinationSerializer(Destination.objects.all(), many=True)

        return Response({ "data" : serializer.data})
    

class DestinationDetailView(APIView):

    @extend_schema(responses={
        200: DestinationDetailSerializer
    }, request=DestinationDetailSerializer)


    def get(self, _, id):
        
        try:
            instance = Destination.objects.get(pk=id)
            serializer = DestinationDetailSerializer(instance)

        except:
            return Response({ "data" : []}, status=HTTP_404_NOT_FOUND)

        return Response({ "data" : serializer.data})


class SearchView(APIView):
    def get(self, req):

        query_name = req.GET.getlist("q")
        
        if not query_name:
            return Response({ "data" : []}, status=HTTP_400_BAD_REQUEST)


        query_name = query_name[0].strip('"\'')

        try:
            instance = Destination.objects.get(name=query_name)
            serializer = SearchSerializer(instance)

        except:
            return Response({ "data" : [] }, status=HTTP_404_NOT_FOUND)
        
        return Response({ "data" : serializer.data })




class CategoryView(APIView):

    @extend_schema(responses={
        200: CategorySerializer
    }, request=CategorySerializer)
    def get(self, _):
        serializer = CategorySerializer(Category.objects.all(), many=True)

        return Response({ "data" : serializer.data})



