from rest_framework import serializers
from .models import Driver, Language, City


class DriverSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')
    language = serializers.CharField(source='language.name')
    
    
    class Meta:
        model = Driver
        fields = ['name', 'mobilenum', 'email', 'city',
                  'district', 'language', 'assigned_truck']
