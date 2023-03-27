from rest_framework import serializers

from api.models import Camera, Coder, Music, Feedback, Light


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['photo', 'title', 'description', 'quantity', 'price']


class CoderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coder
        fields = ['photo', 'title', 'description', 'quantity', 'price']


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['photo', 'title', 'description', 'quantity', 'price']


class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = ['photo', 'title', 'description', 'quantity', 'price']


class FeedbackSerializer(serializers.ModelSerializer):
    fio = serializers.CharField(min_length=3, allow_null=False, allow_blank=False)
    phone_number = serializers.CharField(allow_blank=False, allow_null=False)
    email = serializers.EmailField(allow_null=False, allow_blank=False)
    text = serializers.CharField(allow_blank=False, allow_null=False)

    class Meta:
        model = Feedback
        fields = ['fio', 'phone_number', 'email', 'text']

