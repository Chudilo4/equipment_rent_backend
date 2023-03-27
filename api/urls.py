from django.urls import path
from api.views import FeedbackAPIView, CameraAPIView, MusicAPIView, LightAPIView, CoderAPIView

urlpatterns = [
    path('feedback/', FeedbackAPIView.as_view(), name='feedback'),
    path('camera/', CameraAPIView.as_view(), name='camera'),
    path('music/', MusicAPIView.as_view(), name='music'),
    path('light/', LightAPIView.as_view(), name='light'),
    path('coder/', CoderAPIView.as_view(), name='coder')
]
