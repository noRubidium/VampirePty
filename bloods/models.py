from __future__ import unicode_literals

from django.db import models

from donor.models import Donor
from hospital.models import Hospital
from batmobile.models import Batmobile

import datetime

class Blood(models.Model):
    amount = models.BigIntegerField()
    used = models.BooleanField()
    donorId = models.ForeignKey(Donor, on_delete = models.CASCADE )
    hospitalId = models.ForeignKey(Hospital,  on_delete = models.CASCADE)
    bat_mobileId = models.ForeignKey(Batmobile, on_delete = models.CASCADE)
    arrive_date = models.DateField()
    used_by_date = models.DateField()

    def is_expired(self):
        return self.used_by_date < datetime.date.today()
'''
from donor.models import Donor
from hospital.models import Hospital
from batmobile.models import Batmobile
import time
import random

def strTimeProp(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)

bats = Batmobile.objects.all()
hospitals = Hospital.objects.all()
donors = Donor.objects.all()
for i in xrange(20000):
    amount = random.randint(100,1000)
    used = random.random() < 0.2
    sD = randomDate("2016-05-01","2016-06-14", random.random())
    pD = randomDate(sD,"2016-07-01", random.random())
    b = Blood(amount = amount, used = used, donorId = random.choice(donors), hospitalId = random.choice(hospitals), bat_mobileId = random.choice(bats), arrive_date = sD, used_by_date = pD)
    b.save()
'''
