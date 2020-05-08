from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import *

class ProducerSerializer(ModelSerializer):

    class Meta:
         model = Producer
         fields = '__all__'

class TireSerializer(ModelSerializer):
    producer = StringRelatedField()
    class Meta:
        model = Tire
        fields = ['width' , 'profile' , 'diameter' , 'seoson' , 'producer' ]