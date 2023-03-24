from django.http import JsonResponse
from .models import Driver
from .serializers import DriverSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# filter library
from django_filters import rest_framework as filters

# driver/ - list all driver
@api_view(['POST', ])
def driver_create(request):
    serializer = DriverSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
    
    
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
        

# TEST
from rest_framework.generics import ListAPIView

from django_filters.rest_framework import DjangoFilterBackend

class ProductFilter(filters.FilterSet):

    class Meta:
        model = Driver
        fields = ['email', 'mobilenum']


class DriverList(ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'mobilenum', ]
    
    

    
    