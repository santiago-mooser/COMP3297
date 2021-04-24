
from django.contrib.messages.api import error
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib import messages
from django.template import loader
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import Homepage, New_case, New_location

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
    template = loader.get_template('pages/new_location.html')

    if request.method == 'POST':
        form = New_location(request.POST)

        # check if the form is valid
        if form.is_valid():

            # Extract data from form
            name = form.cleaned_data['location_name']
            loc = form.cleaned_data['location']
            addr = form.cleaned_data['address']
            date = form.cleaned_data['date_of_event']
            description = form.cleaned_data['description_of_event']

            # Create new instance of model Case
            new_loc = Location(
                name=name,
                location=loc,
                Address=addr,
                date_of_event=date,
                Description_of_event=description,
            )
            try:
                new_loc.save()
            except Exception as e:
                print(e)
                messages.error(request, "Internal server error! Please reload page.")
                return HttpResponseRedirect('/add/location')
            
            messages.success(request, "Details successfully saved.")
            # TODO: redirect to location details
            return HttpResponseRedirect('/')

        # If form is invalid
        else:
            messages.error(request, "Please enter valid details.")
            return HttpResponseRedirect('/add/location')
    # If method is not POST (is GET)
    else:
        form = New_location() # empty form instance
    return HttpResponse(template.render({'form': form}, request))

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
                Event=event,
            )
            try:
                new_case.save()
            except Exception as e:
                print(e)
                messages.error(request, "Internal server error! Please reload page.")
                return HttpResponseRedirect('/add/case')
            
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

    template = loader.get_template('pages/location_details.html')
    context = {}
    
    # we assume that there's only 1 location with the same name. Specified in Project req doc I think

    location    = Location.objects.filter(name = loc_name)[0] 
    cases       = Case.objects.filter(event__name__contains = loc_name)
    
    context.update({'location': location, 'cases': cases})

    return HttpResponse(template.render(context, request))

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
