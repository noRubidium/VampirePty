from __future__ import unicode_literals

from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length = 200)

class Donor(models.Model):
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 1)
    blood_type = models.CharField(max_length=2)
    linking_agent = models.ForeignKey(Hospital, on_delete = models.CASCADE)
    DOB = models.DateField()
    address = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    last_verified = models.DateField()
    latitude = models.DecimalField(decimal_places = 2, max_digits = 5)
    longitude = models.DecimalField(decimal_places = 2, max_digits = 5)

class Batmobile(models.Model):
    name = models.CharField(max_length = 200)
    latitude = models.DecimalField(decimal_places = 2, max_digits = 5)
    longitude = models.DecimalField(decimal_places = 2, max_digits = 5)

class Blood(models.Model):
    blood_type = models.CharField(max_length=2)
    amount = models.BigIntegerField()
    used = models.BooleanField()
    donorId = models.ForeignKey(Donor, on_delete = models.CASCADE )
    hospitalId = models.ForeignKey(Hospital,  on_delete = models.CASCADE)
    bat_mobileId = models.ForeignKey(Batmobile, on_delete = models.CASCADE)
    arrive_date = models.DateField()
    used_by_date = models.DateField()
