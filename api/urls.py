from django.urls import path
from api.views import FeedbackAPIView, EquipmentAPIView
urlpatterns = [
    path('feedback/', FeedbackAPIView.as_view(), name='feedback'),
    path('equipments/', EquipmentAPIView.as_view(), name='equipment')
]
