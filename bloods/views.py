from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
import datetime

from .models import Blood
from .forms import BloodForm
from donor.models import Donor

from algorithm import merge_sort, my_filter

# Create your views here.
def index(request):
    donors = Donor.objects.all()
    # bloods = my_filter(bloods, key = lambda x: x.used_by_date >= datetime.date.today() )
    d = dict()
    blood_types = ['A+','A-','B+','B-','AB+','AB-','0+','0-']
    for donor in donors:
        t = donor.blood_type
        amount = donor.blood_set.filter(used = False).aggregate(Sum('amount')).get('amount__sum', 0)
        if(amount == None):
            amount = 0
        d[t] = d.get(t, 0 ) + amount
    blood_stats = [(k,d.get(k,0)) for k in blood_types]
    print blood_stats
    return render(request, 'blood_index.html', {'blood_stats': blood_stats})

def detail(request, bloodId=1):
    try:
        blood = Blood.objects.filter(pk = bloodId)[0]
        donor = blood.donorId
        hospital = blood.hospitalId
        batmobile = blood.bat_mobileId
    except Blood.DoesNotExist:
        raise Http404("Blood does not exist")
    return render(request, 'blood_detail.html', {'hospital': hospital,'blood': blood, 'donor': donor, 'batmobile': batmobile})

def add(request):
    if request.method == 'POST':
        form =BloodForm(request.POST)
        if form.is_valid():
            
            return HttpResponseRedirect('/thanks/')
    else:
        form = BloodForm()

    return render(request, 'blood_add.html', {'form': form})
