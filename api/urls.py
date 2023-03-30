from django.urls import path
from api.views import FeedbackAPIView, SearchEquipmentAPIView

urlpatterns = [
    path('feedback/', FeedbackAPIView.as_view(), name='feedback'),
    path('search/', SearchEquipmentAPIView.as_view(), name='search'),
]
