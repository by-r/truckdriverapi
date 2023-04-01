from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.DriverList.as_view(), name="driver_list"), # return driver list 
    path("/", views.DriverCreate.as_view(), name="driver_create"), # create driver
    path("/<int:pk>", views.DriverDetail.as_view() , name="driver_detail"), # return single driver detail
    
]
