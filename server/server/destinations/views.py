from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Destination
from .serializers import DestinationSerializer


# Create your views here.
class DestinationView(APIView):

    def get(self, req):
        serializer = DestinationSerializer(Destination.objects.all(), many=True)


        return Response(serializer.data)


