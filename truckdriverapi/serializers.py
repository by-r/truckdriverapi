from rest_framework import serializers
from .models import Driver, Language, City, AssignedTruck


class DriverSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')
    language = serializers.CharField(source='language.name')
    number_plate = serializers.CharField(source='assigned_truck.number_plate')
    registration_number = serializers.CharField(source='assigned_truck.registration_number')
    
    class Meta:
        model = Driver
        fields = ['name', 'mobilenum', 'email', 'city',
                  'district', 'language', 'number_plate', 'registration_number']
        
