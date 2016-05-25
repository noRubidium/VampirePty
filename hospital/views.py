from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

import datetime

from .models import Hospital
from hospital.models import Hospital

from algorithm import merge_sort, my_filter

# Create your views here.
def index(request):
    hospital_list = Hospital.objects.all()[:20]
    template = loader.get_template('hospitals/index.html')
    starting_page = 1
    context = {
    'hospital_list': hospital_list,
    'page_id': 1,
    'starting_page': 1,
    'range': xrange(starting_page,starting_page + 5),
    'id': 1
    }
    return render( request,'hospitals/index.html', context )

def page(request,page_id):
    max_page = 5
    page_id = int(page_id)
    try:
        hospital_list = Hospital.objects.all()[(page_id - 1) * 20: page_id * 20]
    except:
        hospital_list = Hospital.objects.all()[:20]
        page_id = 1
    if page_id - 2 <= 0:
        starting_page = 1
    elif page_id + 2 > max_page:
        starting_page = max_page - 4
    else:
        starting_page = page_id - 2
    template = loader.get_template('hospitals/index.html')
    context = {
        'hospital_list': hospital_list,
        'page_id': page_id,
        'starting_page': starting_page,
        'range':  xrange(starting_page,starting_page + 5),
        'id': 1
    }
    return HttpResponse(template.render(context, request))

def detail(request,hospital_id):
    try:
        hospital = Hospital.objects.get(pk=hospital_id)
        bloods = hospital.blood_set.all()
        bloods = my_filter(bloods, key = lambda x: (not x.used) and x.used_by_date >= datetime.date.today() )
        d = dict()
        blood_types = ['A+','A-','B+','B-','AB+','AB-','0+','0-']
        for blood in bloods:
            d[str(blood.donorId.blood_type)] = d.get(str(blood.donorId.blood_type), 0 ) + blood.amount
        blood_stats = [(k,d.get(k,0)) for k in blood_types]
    except Hospital.DoesNotExist:
        raise Http404("Hospital does not exist")
    return render(request, 'hospitals/detail.html', {'hospital': hospital,'blood_stats': blood_stats, 'id': hospital_id})

def blood_detail(request,hospital_id):
    try:
        hospital = Hospital.objects.get(pk=hospital_id)
        bloods = hospital.blood_set.all()
        bloods_1 = my_filter(bloods, key = lambda x: not x.used)
        bloods = bloods_1[:]
        merge_sort(bloods, bloods_1, key = lambda x: x.used_by_date)
    except Hospital.DoesNotExist:
        raise Http404("Hospital does not exist")
    return render(request, 'hospitals/blood_detail.html', {'blood_list':bloods,'hospital': hospital, 'id': hospital_id, 'today': datetime.date.today()})

def donor_detail(request,hospital_id):
    try:
        hospital = Hospital.objects.get(pk=hospital_id)
        donors = hospital.donor_set.all()
    except Hospital.DoesNotExist:
        raise Http404("Hospital does not exist")
    return render(request, 'hospitals/donor_detail.html', {'hospital': hospital,'blood_list': bloods, 'donors': donors, 'id': hospital_id})
