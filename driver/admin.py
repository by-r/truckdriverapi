from django.contrib import admin
from .models import Driver, City, Language, AssignedTruck

admin.site.register(Driver)
admin.site.register(City)
admin.site.register(Language)
admin.site.register(AssignedTruck)
