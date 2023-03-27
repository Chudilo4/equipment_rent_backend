import os

from rest_framework import status
from rest_framework.views import APIView
from api.models import Camera, Coder, Light, Music
from api.serializers import CameraSerializer, FeedbackSerializer, CoderSerializer, MusicSerializer, LightSerializer

from rest_framework.response import Response
import requests
from dotenv import load_dotenv

load_dotenv('.env')


# Create your views here.
class CameraAPIView(APIView):

    def get(self, request, *args, **kwargs):
        equipment = Camera.objects.all()
        serializer = CameraSerializer(instance=equipment, many=True, context={'request': request})
        return Response(serializer.data, status.HTTP_200_OK)


class MusicAPIView(APIView):

    def get(self, request, *args, **kwargs):
        equipment = Music.objects.all()
        serializer = MusicSerializer(instance=equipment, many=True, context={'request': request})
        return Response(serializer.data, status.HTTP_200_OK)


class LightAPIView(APIView):

    def get(self, request, *args, **kwargs):
        equipment = Light.objects.all()
        serializer = LightSerializer(instance=equipment, many=True, context={'request': request})
        return Response(serializer.data, status.HTTP_200_OK)


class CoderAPIView(APIView):

    def get(self, request, *args, **kwargs):
        equipment = Coder.objects.all()
        serializer = CoderSerializer(instance=equipment, many=True, context={'request': request})
        return Response(serializer.data, status.HTTP_200_OK)


class FeedbackAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = os.getenv('BOT_TOKEN')
            method = 'sendMessage'
            text = 'Вам пришла заявка\n' \
                   f'От кого : {serializer.data["fio"]}\n' \
                   f'Телефонный номер: {serializer.data["phone_number"]}\n' \
                   f'EMAIL : {serializer.data["email"]}\n' \
                   f'ЧТО хочет : {serializer.data["text"]}\n'
            requests.get('https://api.telegram.org/bot{0}/{1}'.format(token, method),
                         data={'chat_id': os.getenv('CHAT_ID'), 'text': text}).json()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
