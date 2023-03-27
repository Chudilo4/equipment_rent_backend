from django.urls import path
from api.views import FeedbackAPIView, SearchEqAPIView

urlpatterns = [
    path('feedback/', FeedbackAPIView.as_view(), name='feedback'),
    path('search/', SearchEqAPIView.as_view(), name='search'),
]
