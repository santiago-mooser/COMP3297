from django.shortcuts import render

from .forms import Homepage

# Create your views here.


def homepage(request):
    form = Homepage()
    return render(request, 'base.html', {'form': form})

def add_location(request):
    return

def add_case(request):
    return

def location_details(request, loc_name):
    return

def case_details(request, loc_name):
    return

def proxy(request):
    return