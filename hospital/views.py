from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import template


import re
import datetime

from .models import Hospital
from hospital.models import Hospital

from algorithm import merge_sort, my_filter

register = template.Library()


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
        bloods = my_filter(bloods, key = lambda x: (not x.used) and not x.is_expired() )
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
        hide_expired = request.GET.get('hide_expired', False)
        bloodFilter = request.GET.getlist('blood_type', ["A","B", "AB", "0"])
        bloodSignFilter = request.GET.getlist('blood_sign', ["+","-"])
        bloodFiltering = [str(x) +y for x in bloodFilter for y in bloodSignFilter]
        bloods = hospital.blood_set.all()
        bloods_1 = my_filter(bloods, key = lambda x:  (not x.used) and x.donorId.blood_type in bloodFiltering )
        if hide_expired:
            bloods_1 = my_filter(bloods_1, key = lambda x: not x.is_expired())
        bloods = bloods_1[:]
        merge_sort(bloods, bloods_1, key = lambda x: x.used_by_date)
        paginator = Paginator(bloods, 25)
        page = request.GET.get('page')

        try:
            bloods = paginator.page(page)
        except PageNotAnInteger:
            bloods = paginator.page(1)
        except EmptyPage:
            bloods = paginator.page(paginator.num_pages)
    except Hospital.DoesNotExist:
        raise Http404("Hospital does not exist")
    return render(request, 'hospitals/blood_detail.html',
        {'blood_list':bloods,
        'hospital': hospital,
        'id': hospital_id,
        'hide_expired': hide_expired,
        'blood_filter': bloodFilter,
        })

def donor_detail(request,hospital_id):
    try:
        hospital = Hospital.objects.get(pk=hospital_id)
        donors = hospital.donor_set.all()
    except Hospital.DoesNotExist:
        raise Http404("Hospital does not exist")
    return render(request, 'hospitals/donor_detail.html', {'hospital': hospital,'donors': donors, 'id': hospital_id})

@register.simple_tag
def url_replace(request, field, value):

    dict_ = request.GET.copy()

    dict_[field] = value

    return dict_.urlencode()
