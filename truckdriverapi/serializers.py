from rest_framework import serializers
from .models import Driver, Language, City, AssignedTruck

class AssignedTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedTruck
        fields = ['number_plate', 'registration_number']

class DriverSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')
    language = serializers.CharField(source='language.name')
    
    assigned_truck = AssignedTruckSerializer(required=True)
    
    class Meta:
        model = Driver
        fields = ['name', 'mobilenum', 'email', 'city',
                  'district', 'language', 'assigned_truck']
        
    def create(self, validated_data):
        assigned_truck_data = validated_data.pop('assigned_truck')
        assigned_truck = AssignedTruckSerializer.create(AssignedTruckSerializer(), validated_data=assigned_truck_data)
        driver, created = Driver.objects.update_or_create(assigned_truck=assigned_truck)
        return driver