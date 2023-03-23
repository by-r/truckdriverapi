from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path("driver/", views.driver_list, name="driver_list"),
    path("driver/<int:pk>", views.driver_detail, name="driver_detail"),
]
