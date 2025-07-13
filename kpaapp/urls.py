from django.urls import path
from .views import WheelSpecificationAPIView, BogieChecksheetAPIView

urlpatterns = [
    path('forms/wheel-specifications/', WheelSpecificationAPIView.as_view(), name='create-wheel-spec'),
    path('forms/bogie-checksheet/', BogieChecksheetAPIView.as_view(), name='bogie-checksheet'),
]
