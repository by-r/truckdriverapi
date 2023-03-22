from rest_framework import serializers
from .models import Driver, Language, City


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['name', 'mobilenum', 'email', 'city',
                  'district', 'language', 'assigned_truck']
