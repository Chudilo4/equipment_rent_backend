import logging


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Category
from api.serializers import EquipmentSerializer, FeedbackSerializer, EquipmentRentSerializer
from service.telegram import send_telegram

logger = logging.getLogger(__name__)


class SearchEquipmentAPIView(APIView):

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        try:
            equipment = Category.objects.get(title=query).equipments.all()
        except Category.DoesNotExist:
            return Response({'Такой категории нет'}, status.HTTP_400_BAD_REQUEST)
        serializer = EquipmentSerializer(instance=equipment, many=True,
                                         context={'request': request})
        logger.info(f"{request.META['REMOTE_ADDR']} получил список оборудования")
        return Response(serializer.data, status.HTTP_200_OK)


class FeedbackAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.data.get('email')
            send_telegram(serializer)
            logger.info(f"{request.META['REMOTE_ADDR']} создал заявку")
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class EquipmentRentAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = EquipmentRentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_telegram(serializer)
            logger.info(f"{request.META['REMOTE_ADDR']} создал заявку")
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
