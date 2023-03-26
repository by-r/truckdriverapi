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
        fields = ['name', 'mobilenum', 'email', 'city', 'district', 'language', 'assigned_truck']

    def create(self, validated_data):
        assigned_truck_data = validated_data.pop('assigned_truck')
        assigned_truck = AssignedTruck.objects.create(**assigned_truck_data)
        language_data = validated_data.pop('language')
        language = Language.objects.get_or_create(name=language_data['name'])[0]
        city_data = validated_data.pop('city')
        city = City.objects.get_or_create(name=city_data['name'])[0]
        driver = Driver.objects.create(
            assigned_truck=assigned_truck,
            language=language,
            city=city,
            **validated_data
        )
        return driver