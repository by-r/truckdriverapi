from django.db import models


class Driver(models.Model):

    name = models.CharField(max_length=255)
    mobilenum = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    district = models.CharField(max_length=50, blank=True, null=True)
    language = models.ForeignKey("Language", on_delete=models.CASCADE)
    assigned_truck = models.OneToOneField("AssignedTruck", on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name

class AssignedTruck(models.Model):
    number_plate = models.CharField(max_length=10, unique=True)
    registration_number = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.number_plate} - {self.registration_number}"

class City(models.Model):

    CITIES_IN_MALAYSIA = [
        ('JHR', 'Johor'),
        ('KDH', 'Kedah'),
        ('KTN', 'Kelantan'),
        ('KUL', 'Kuala Lumpur'),
        ('LBN', 'Labuan'),
        ('MLK', 'Melaka'),
        ('NSN', 'Negeri Sembilan'),
        ('PHG', 'Pahang'),
        ('PRK', 'Perak'),
        ('PLS', 'Perlis'),
        ('SBH', 'Sabah'),
        ('SGR', 'Selangor'),
        ('TRG', 'Terengganu'),

    ]
    name = models.CharField(
        max_length=3, choices=CITIES_IN_MALAYSIA, default=None)

    class Meta:
        verbose_name = ("City")
        verbose_name_plural = ("Cities")

    def __str__(self):
        return self.name


class Language(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
