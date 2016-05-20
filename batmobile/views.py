from django.shortcuts import render
from django.http import HttpResponse

# import names
# import random

from .models import Batmobile
# Create your views here.
def index(request):
    l = []
    # # init script
    # for i in xrange(300):
    #     name = names.get_last_name()
    #     b = Batmobile(name = name, latitude = random.random() * 180 - 90, longitude = random.random() * 360 - 180)
    #     l.append(b)
    #     b.save()
    return HttpResponse("Hello this is batmobile" + l.__str__())
