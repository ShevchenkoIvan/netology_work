from django.urls import path

from .views import SensorView, OneSensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', OneSensorView.as_view()),
    path('measurement/', MeasurementView.as_view()),
]
