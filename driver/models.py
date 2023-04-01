from django.db import models


class Driver(models.Model):
    
    name = models.CharField(max_length=255)
    mobilenum = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    city = models.ForeignKey("City", on_delete=models.CASCADE, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    language = models.ForeignKey("Language", on_delete=models.CASCADE,blank=True, null=True)
    assigned_truck = models.OneToOneField("AssignedTruck", on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name

class AssignedTruck(models.Model):
    number_plate = models.CharField(max_length=10, unique=True)
    registration_number = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.number_plate} - {self.registration_number}"

class City(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = ("Cities")

    def __str__(self):
        return self.name


class Language(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name