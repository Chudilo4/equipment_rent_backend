from rest_framework import serializers

from api.models import Equipment, Feedback


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['photo', 'title', 'description', 'quantity', 'price']


class FeedbackSerializer(serializers.ModelSerializer):
    fio = serializers.CharField(min_length=3, allow_null=False, allow_blank=False)
    phone_number = serializers.CharField(allow_blank=False, allow_null=False)
    email = serializers.EmailField(allow_null=False, allow_blank=False)
    text = serializers.CharField(allow_blank=False, allow_null=False)

    class Meta:
        model = Feedback
        fields = ['fio', 'phone_number', 'email', 'text']

