from django.http.response import HttpRespons, HttpResponse
from django.template import loader
from .models import *
from django.contrib import messages
# Create your views here.


def homepage(request):
    return 


def add_location(request):
    return

def add_case(request):
    return

def location_details(request, loc_name):
    template = loader.get_template('pages/location_details.html')
    context = {}

    try:
        location = Location.objects.get(name=loc_name)
    except:
        messages.error(request, "Location not found!")
        return HttpResponse(template.render(context, request))


    context.update({
        "name": location.name,
        "location": location.location,
        "address": location.address,
        "date_of_event": location.date_of_event,
        "description_of_event": location.description_of_event,
    })

    return HttpResponse(template.render(context, request))

def case_details(request, loc_name):
    return

def proxy(request):
    return