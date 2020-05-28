from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from .serializers import *

class ProducerViewSet(ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class TireViewSet(ModelViewSet):
    queryset = Tire.objects.all()
    serializer_class = TireSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ['price', 'seoson']
    search_fields = ['width', 'profile', 'diameter']


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class DiscViewSet(ModelViewSet):
    queryset = Disc.objects.all()
    serializer_class = DiscSerializer
