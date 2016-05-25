from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

import datetime

from .models import Batmobile
from batmobile.models import Batmobile

from algorithm import merge_sort, my_filter

# Create your views here.
def index(request):
    batmobile_list = Batmobile.objects.all()[:20]
    template = loader.get_template('batmobiles/index.html')
    starting_page = 1
    context = {
    'batmobile_list': batmobile_list,
    'page_id': 1,
    'starting_page': 1,
    'range': xrange(starting_page,starting_page + 5),
    }
    return render( request,'batmobiles/index.html', context )

def page(request,page_id):
    max_page = 5
    page_id = int(page_id)
    try:
        batmobile_list = Batmobile.objects.all()[(page_id - 1) * 20: page_id * 20]
    except:
        batmobile_list = Batmobile.objects.all()[:20]
        page_id = 1
    if page_id - 2 <= 0:
        starting_page = 1
    elif page_id + 2 > max_page:
        starting_page = max_page - 4
    else:
        starting_page = page_id - 2
    template = loader.get_template('batmobiles/index.html')
    context = {
        'batmobile_list': batmobile_list,
        'page_id': page_id,
        'starting_page': starting_page,
        'range':  xrange(starting_page,starting_page + 5),
    }
    return HttpResponse(template.render(context, request))

def detail(request,batmobile_id):
    try:
        batmobile = Batmobile.objects.get(pk=batmobile_id)
        bloods = batmobile.blood_set.all()
        bloods = my_filter(bloods, key = lambda x: (not x.used) and x.used_by_date >= datetime.date.today() )
        d = dict()
        blood_types = ['A+','A-','B+','B-','AB+','AB-','0+','0-']
        for blood in bloods:
            d[str(blood.donorId.blood_type)] = d.get(str(blood.donorId.blood_type), 0 ) + blood.amount
        blood_stats = [(k,d.get(k,0)) for k in blood_types]
    except Batmobile.DoesNotExist:
        raise Http404("Batmobile does not exist")
    return render(request, 'batmobiles/detail.html', {'batmobile': batmobile,'blood_stats': blood_stats, 'id': batmobile_id})

def blood_detail(request,batmobile_id):
    try:
        batmobile = Batmobile.objects.get(pk=batmobile_id)
        bloods = batmobile.blood_set.all()
        bloods_1 = my_filter(bloods, key = lambda x: not x.used)
        bloods = bloods_1[:]
        merge_sort(bloods, bloods_1, key = lambda x: x.used_by_date)
    except Batmobile.DoesNotExist:
        raise Http404("Batmobile does not exist")
    return render(request, 'batmobiles/blood_detail.html', {'blood_list':bloods,'batmobile': batmobile, 'id': batmobile_id})

def donor_detail(request,batmobile_id):
    try:
        batmobile = Batmobile.objects.get(pk=batmobile_id)
        donors = batmobile.donor_set.all()
    except Batmobile.DoesNotExist:
        raise Http404("Batmobile does not exist")
    return render(request, 'batmobiles/donor_detail.html', {'batmobile': batmobile,'blood_list': bloods, 'donors': donors, 'id': batmobile_id})
