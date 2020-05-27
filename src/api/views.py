from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *

class ProducerViewSet(ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class TireViewSet(ModelViewSet):
    queryset = Tire.objects.all()
    serializer_class = TireSerializer

    def list(self, request, *args, **kwargs):

        page = self.paginate_queryset(self.get_queryset())

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(serializer.data)

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class DiscViewSet(ModelViewSet):
    queryset = Disc.objects.all()
    serializer_class = DiscSerializer