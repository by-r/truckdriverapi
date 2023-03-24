from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("driver", views.DriverList.as_view(), name="driver_list"), # return driver list 
    path("driver/", views.driver_create, name="driver_create"), # create driver
    path("driver/<int:pk>", views.driver_detail, name="driver_detail"), # return single driver detail
    
]
