# Generated by Django 4.1.7 on 2023-03-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truckdriverapi', '0002_assignedtruck_remove_driver_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]