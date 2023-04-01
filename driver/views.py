from django.shortcuts import render
from .models import Driver
from .serializers import DriverSerializer
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

# filter library
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

# Filterset function for DriverList
class DriverFilter(filters.FilterSet):
    class Meta:
        model = Driver
        fields = ( 'email', 'mobilenum', 'language', 'assigned_truck')

# driver - list all driver with filters
class DriverList(ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = DriverFilter

# driver/ - create single driver
class DriverCreate(APIView):
    def post(self, request, format=None):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# driver/<id> - returns single driver
class DriverDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        driver = self.get_object(pk)
        serializer = DriverSerializer(driver)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        driver = self.get_object(pk)
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        driver = self.get_object(pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
