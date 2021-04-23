from django.shortcuts import render

from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import Homepage
from .models import Location

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
    return

def add_case(request):
    return

def location_details(request, loc_name):
    return

def case_details(request, loc_name):
    return

def proxy(request):
    return