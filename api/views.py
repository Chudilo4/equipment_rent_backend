from rest_framework import status
from rest_framework.views import APIView
from api.models import Equipment
from api.serializers import EquipmentSerializer, FeedbackSerializer
from rest_framework.response import Response
import requests


# Create your views here.
class EquipmentAPIView(APIView):

    def get(self, request, *args, **kwargs):
        equipment = Equipment.objects.all()
        serializer = EquipmentSerializer(instance=equipment, many=True , context={'request': request})
        return Response(serializer.data, status.HTTP_200_OK)


class FeedbackAPIView(APIView):

    def post(self, request, *args, **kwargs):
        print(requests.post('https://api.telegram.org/bot5818251636:AAFIOC9Q3u3Q7cfMms0KqWcuhWXZUZTibE8/getCommand=timer'))
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
