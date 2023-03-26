from .models import Driver
from .serializers import DriverSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView

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
    #filterset_fields = ['email', 'mobilenum', ]
    filterset_class = DriverFilter

# driver/ - create single driver
@api_view(['POST', ])
def driver_create(request):
    serializer = DriverSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    
# driver/<id> - returns single driver
@api_view(['GET', 'PUT', 'DELETE'])
def driver_detail(request, pk):
    
    try:
        driver = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DriverSerializer(driver)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        




    
    