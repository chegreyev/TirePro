from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import *

class ProducerSerializer(ModelSerializer):

    class Meta:
         model = Producer
         fields = '__all__'

class TireSerializer(ModelSerializer):
    producer = SlugRelatedField(queryset=Producer.objects.all(), slug_field='name')
    class Meta:
        model = Tire
        fields = ['width' , 'profile' , 'diameter' , 'seoson' , 'producer']