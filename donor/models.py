from __future__ import unicode_literals

from django.db import models

from hospital.models import Hospital
# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 1)
    blood_type = models.CharField(max_length=3)
    linking_agent = models.ForeignKey(Hospital, on_delete = models.CASCADE)
    DOB = models.DateField()
    address = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    last_verified = models.DateField()
    latitude = models.DecimalField(decimal_places = 2, max_digits = 5)
    longitude = models.DecimalField(decimal_places = 2, max_digits = 5)
