from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from .models import Sensor
from .serializers import SensorDetailSerializer, MeasurementSerializer


class SensorView(ListAPIView, CreateAPIView):
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = Sensor.objects.values('id', 'name', 'description')
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class MeasurementView(CreateAPIView):
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        serializer.save()


class OneSensorView(RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def perform_update(self, serializer):
        serializer.save()


