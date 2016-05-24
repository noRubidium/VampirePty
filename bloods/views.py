from django.shortcuts import render
from django.http import HttpResponse

import datetime

from .models import Blood

from algorithm import merge_sort, my_filter

# Create your views here.
def index(response):
    bloods = Blood.objects.filter(used = False)
    bloods = my_filter(bloods, key = lambda x: x.used_by_date >= datetime.date.today() )
    d = dict()
    blood_types = ['A+','A-','B+','B-','AB+','AB-','0+','0-']
    i = 0
    for blood in bloods:
        print i
        i += 1
        t = str(blood.donorId.blood_type)
        d[t] = d.get(t, 0 ) + blood.amount
    blood_stats = [(k,d.get(k,0)) for k in blood_types]
    print blood_stats
    return render(request, 'index.html', {'blood_stats': blood_stats})
