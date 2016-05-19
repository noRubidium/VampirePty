from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(response):
    return HttpResponse('HelloWorld')
# https://docs.djangoproject.com/en/1.9/intro/tutorial02/
