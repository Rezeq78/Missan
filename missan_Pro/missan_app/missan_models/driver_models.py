from django.db import models



class DriverInfo(models.Model):


    iqama_number = models.CharField(unique=True,max_length=10)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(blank=True,max_length=30)
    fourth_name = models.CharField(blank=True,max_length=30)
    last_name = models.CharField(max_length=30)
    joining_date = models.DateField()
    city = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    current_application = models.CharField(blank=True,max_length=50)
    previous_application = models.CharField(blank=True,max_length=50)
    iqama_expiry_date = models.DateField()
    driver_license_expiry_date = models.DateField()
    sponsor_name = models.CharField(max_length=100)
    knows_aout_us = models.CharField(blank=True,max_length=200)
    car_type = models.CharField(max_length=30)
    car_plate_number = models.CharField(max_length=30)
    car_color = models.CharField(max_length=30)
    car_model = models.CharField(max_length=4)
