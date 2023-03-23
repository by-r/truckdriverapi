from django.http import JsonResponse
from .models import Driver
from .serializers import DriverSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# driver/ - list all driver
@api_view(['GET', 'POST'])
def driver_list(request):
    
    if request.method == 'GET':
        driver = Driver.objects.all()
        serializer = DriverSerializer(driver, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
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
        
    