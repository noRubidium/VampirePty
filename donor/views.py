from django.shortcuts import render
from django.http import HttpResponse

from faker import Faker
from faker import Factory
from .models import Donor
import random

# Create your views here.
def index(request):
    l = []
    # fake = Faker()
    # fake = Factory.create()
    # # init script
    # for i in xrange(4):
    #     user = fake.profile()
    #     d = Donor( password = "seng2011", blood_type = user['blood_group'], gender = user['sex'], latitude = float(user['current_location'][0]),longitude = float(user['current_location'][1]),DOB = user['birthdate'], username = user['username'], address = user['address'], name = user['name'], linking_agent = Hospital.objects.filter(pk = random.randint(1,101))[0], phone = user['ssn'], last_verified = fake.date_time_this_year(before_now=True, after_now=False))
    #     # if bt < 0.36:
    #     #     bt = "A+"
    #     # elif bt < 0.42:
    #     #     bt = "A-"
    #     # elif bt < 0.51:
    #     #     bt = "B+"
    #     # elif bt < 0.52:
    #     #     bt = "B-"
    #     # elif bt < 0.55:
    #     #     bt = "AB+"
    #     # elif bt < 0.56:
    #     #     bt = "AB-"
    #     # elif bt < 0.93:
    #     #     bt = "O+"
    #     # else:
    #     #     bt = "O-"
    #
    #     l.append(d)
    #     # b.save()
    return HttpResponse("Hello this is donor" + l.__str__())
