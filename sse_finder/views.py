from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.template import loader
from django.http.response import HttpResponse, HttpResponseRedirect
# Create your views here.


def homepage(request):
    return 


def add_location(request):
    return

def add_case(request):
    return

def location_details(request, loc_name):
    return

def case_details(request, case_num):
    template = loader.get_template('pages/case_details.html')
    context = {}

    try:
        case = Case.objects.get(case_number=case_num)
    except:
        messages.error(request, "Case not found!")
        return HttpResponse(template.render(context, request))

    context.update(case.get_details())

    return HttpResponse(template.render(context, request))



def proxy(request):
    return