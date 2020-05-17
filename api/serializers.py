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

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ['mark' , 'model', 'year', 'modification', 'type_size', 'tire']

    def to_representation(self, instance):
        representation = super(CarSerializer, self).to_representation(instance)
        data = Tire.objects.get(id = representation['tire'])
        representation['tire'] = TireSerializer(data).data
        return representation