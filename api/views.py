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