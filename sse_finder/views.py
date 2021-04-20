from django.shortcuts import render

from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import Homepage

# Create your views here.


def homepage(request):
    # First, like always, load the HTML template with no context
    template = loader.get_template('base.html')
    context = {}
    form = Homepage()

    context.update({ "form": form })

    return HttpResponse(template.render(context, request))

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