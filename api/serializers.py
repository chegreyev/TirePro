from rest_framework.serializers import ModelSerializer
from .models import *

class ProducerSerializer(ModelSerializer):

    class Meta:
         model = Producer
         fields = '__all__'

class TireSerializer(ModelSerializer):

    class Meta:
        model = Tire
        fields = ['width' , 'profile' , 'diameter' , 'seoson' , 'producer' ]