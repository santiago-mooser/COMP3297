from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.template import loader
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import *
from django import forms
# Create your views here.


def homepage(request):
    # First, like always, load the HTML template with no context

    if request.method == 'POST':

        form = Homepage(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

    template = loader.get_template('pages/home.html')
    context = {}
    form = Homepage()

    context.update({ "form": form })

    locations = Location.objects.all()
    for location in locations:
        location.cases = 10
    context.update({'locations': locations})

    return HttpResponse(template.render(context, request))

def add_location(request):

    if request.method == 'POST':
        form = New_location(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            #return HttpResponseRedirect()
    else:
        form = New_location()

    template = loader.get_template('pages/add_location.html')
    context = {}
    context.update({'form':form})

    return HttpResponse(template.render(context, request))

def add_case(request):

    if request.method == 'POST':
        form = New_case(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            #return HttpResponseRedirect()
    else:
        form = New_case()

    template = loader.get_template('pages/add_case.html')
    context = {}
    context.update({'form':form})

    return HttpResponse(template.render(context, request))

def location_details(request, loc_name):
    template = loader.get_template('pages/location_details.html')
    context = {}

def case_details(request, loc_name):
    return

    try:
        case = Case.objects.get(case_number=case_num)
    except:
        messages.error(request, "Case not found!")
        return HttpResponse(template.render(context, request))

    context.update(case.get_details())

    return HttpResponse(template.render(context, request))



def proxy(request):
    return
