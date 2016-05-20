from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader


from .models import Hospital
from hospital.models import Hospital
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
    }
    return HttpResponse(template.render(context, request))

def detail(request,hospital_id):
    try:
        hospital = Hospital.objects.get(pk=hospital_id)
        bloods = hospital.blood_set.all()
        donors = hospital.donor_set.all()
    except Hospital.DoesNotExist:
        raise Http404("Hospital does not exist")
    return render(request, 'hospitals/detail.html', {'hospital': hospital})
