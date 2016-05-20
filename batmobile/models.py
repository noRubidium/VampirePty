from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Batmobile(models.Model):
    name = models.CharField(max_length = 200)
    latitude = models.DecimalField(decimal_places = 2, max_digits = 5)
    longitude = models.DecimalField(decimal_places = 2, max_digits = 5)

    def __str__(self):
        return self.name + str(self.latitude) + str(self.longitude)
