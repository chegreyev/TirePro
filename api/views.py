from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class ProducerViewSet(ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class TireViewSet(ModelViewSet):
    queryset = Tire.objects.all()
    serializer_class = TireSerializer

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class DiscViewSet(ModelViewSet):
    queryset = Disc.objects.all()
    serializer_class = DiscSerializer