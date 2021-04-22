from django.contrib.messages.api import error
from django.shortcuts import render

from django.shortcuts import redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import Homepage, New_case, New_location
from django.contrib import messages
from .models import *

# Create your views here.


def homepage(request):
    # First, like always, load the HTML template with no context
    template = loader.get_template('pages/home.html')
    context = {}
    form = Homepage()

    context.update({ "form": form })

    return HttpResponse(template.render(context, request))

def add_location(request):
    return

def add_case(request):
    template = loader.get_template('pages/new_case.html')

    if request.method == 'POST':
        form = New_case(request.POST)

        # check if the form is valid
        if form.is_valid():

            # Extract data from form
            name     = form.cleaned_data['case_name']
            num_case = form.cleaned_data['case_number']
            pid      = form.cleaned_data['personal_id']
            dob      = form.cleaned_data['date_of_birth']
            doo      = form.cleaned_data['date_of_onset']
            dot      = form.cleaned_data['date_of_test']
            event    = form.cleaned_data['case_event']

            # Create new instance of model Case
            new_case = Case(
                name=name,
                case_number=num_case,
                personal_id=pid,
                date_of_birth=dob,
                date_of_onset=doo,
                date_of_test=dot,
                # TODO: add class variable Event in forms.py
                Event=event,
            )
            try:
                new_case.save()
            except Exception as e:
                print(e)
                messages.error(request, "Internal server error! Please reload page.")
                # TODO: redirect to homepage
                return HttpResponseRedirect('/')
            
            messages.success(request, "Details successfully saved.")
            # TODO: redirect to case details
            return HttpResponseRedirect('/')

        # If form is invalid
        else:
            messages.error(request, "Please enter valid details.")
            return HttpResponseRedirect('/add/case')
    # If method is not POST
    else:
        form = New_case() # empty form instance
    return HttpResponse(template.render({'form': form}, request))

def location_details(request, loc_name):
    return

def case_details(request, loc_name):
    return

def proxy(request):
    return
