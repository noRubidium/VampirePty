from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(response):
    return HttpResponse('HelloWorld')
def hospital_index(response, hospital_id):
    return HttpResponse('HelloWorld')
