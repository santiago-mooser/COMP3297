from django import template
from .models import *
from django.contrib import messages
from django.template import loader
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from .forms import *
import datetime

@login_required(login_url='/login')
def homepage(request):

    template = loader.get_template('pages/home.html')
    context = {}

    if request.method == 'POST':

        form = Homepage(request.POST)

        if form.is_valid():

            locations = Location.objects.filter(date_of_event__range=[form.cleaned_data["date_from_range"], form.cleaned_data["date_to_range"]])

            events=[]

            for event in locations:
                events.append(event.get_details().get("location"))

            context.update({'locations': events })
            context.update({'form': form})

            return HttpResponse(template.render(context, request))

        else:

            messages.error(request, "Invalid dates!")

    form = Homepage()
    locations = Location.objects.all()

    events=[]

    for event in locations:
        events.append(event.get_details().get("location"))
    
    events = sorted(events, key = lambda i: i['case_num'], reverse=True)

    context.update({'form': form })
    context.update({'locations': events})

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def add_location(request):

    template = loader.get_template('pages/new_location.html')
    context={}

    if request.method == 'POST':
        form = New_location(request.POST)

        # check if the form is valid
        if form.is_valid():

            # Extract data from form
            name = form.cleaned_data['venue_name']
            loc = form.cleaned_data['building_name']
            date = form.cleaned_data['date_of_event']
            description = form.cleaned_data['description_of_event']

            # Create new instance of model Case
            new_loc = Location(
                venue_name=name,
                building_name=loc,
                date_of_event=date,
                description_of_event=description,
            )

            #Try to save data
            try:
                new_loc.save()

            #Show error message if not saved successfully
            except Exception as e:

                print(e)
                messages.error(request, "Internal server error! Please reload page.")

                context.update({'form': form})
                return HttpResponse(template.render(context, request))

            #Redirect to location_details if successfully added
            messages.success(request, "Details successfully saved.")
            return redirect('/location/'+new_loc.venue_name)

        # If form invalid, render this page w/ submitted details
        else:
            messages.error(request, "Please enter valid details.")
            context.update({'form': form})
            return HttpResponse(template.render(context, request))

    # If method is not POST, render this page w/ empty form
    form = New_location()
    context.update({'form': form})

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def add_case(request):

    template = loader.get_template('pages/new_case.html')
    context={}

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
            events   = form.cleaned_data['case_event']

            # Create new instance of model Case
            new_case = Case(
                name=name,
                case_number=num_case,
                personal_id=pid,
                date_of_birth=dob,
                date_of_onset=doo,
                date_of_test=dot,
            )

            # Try to save data
            try:
                new_case.save()

            # If can't save data, handle and reload page w/ same details
            except Exception as e:
                print(e)
                messages.error(request, "Internal server error! Please reload page.")

                context.update({'form': form})
                return HttpResponse(template.render(context, request))
            
            for event in events:
                try:
                    event.add_attendee(new_case)
                except:
                    messages.error(request, "Failed to add case to "+event+": Date missmatch.")
            
            # If successfully saved, redirect to case_details
            messages.success(request, "Details successfully saved.")
            return redirect('/case/'+new_case.case_number)

        # If form is invalid show error message but keep details
        else:
            messages.error(request, "Please enter valid details.")
            context.update({'form': form})
            return HttpResponse(template.render(context, request))


    # Otherwise show render this page with empty form
    form = New_case()
    context.update({'form':form})

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def location_details(request, loc_name):

    template = loader.get_template('pages/location_details.html')
    context = {}

    # we assume that there's only 1 location with the same name. Specified in Project req doc I think

    location    = Location.objects.get(venue_name = loc_name) 
    cases       = location.attendees.all()
    
    context.update(location.get_details())
    context.update({"cases":cases})

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def case_details(request, case_num):

    template = loader.get_template('pages/case_details.html')
    context = {}

    try:
        case = Case.objects.get(case_number=case_num)
        events = case.location_set.all()
    except:
        messages.error(request, "Case not found!")
        return HttpResponse(template.render(context, request))

    context.update(case.get_details())
    details={}
    for event in events:
        details.update({event.venue_name: event.get_details().get("location")})
        context.update({"events":details})

    return HttpResponse(template.render(context, request))



def find_case(request):
    
    template = loader.get_template('pages/find_case.html')
    context = {}

    if request.method == 'POST':
        form = Find_case(request.POST)

        # check if the form is valid
        if form.is_valid():

            # Extract data from form
            case_num     = form.cleaned_data['case_number']
            
            # Retrive case from database, show error if not exists
            try:
                case = Case.objects.get(case_number=case_num)
                return redirect('/case/'+case.case_number)

            except Case.DoesNotExist:
                messages.error(request, "Case not found!")
                return redirect('/find/error')

        # if invalid form
        else:
            messages.error(request, "Please enter valid details.")
            context.update({'form': form})
            return HttpResponse(template.render(context, request))
    
    form = Find_case()
    context.update({'form':form})

    return HttpResponse(template.render(context, request))



def find_error(request):
    template = loader.get_template('pages/find_error.html')
    context = {}

    return HttpResponse(template.render(context, request))



def login_view(request):
    template = loader.get_template('pages/login.html')
    context = {}

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None: # user is authenticated
                login(request, user)
                # redirect to home
                return redirect('/home')
            else:
                # return login error page
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    context.update({'login_form': form})

    return HttpResponse(template.render(context,request))



def edit_case(request, case_num):
    template = loader.get_template('pages/edit_case.html')
    context = {}

    try:
        case = Case.objects.get(case_number=case_num)

    except Case.DoesNotExist:
        messages.error(request, "Case does not exist!")
        return redirect('/home/')


    if request.method == 'POST':
        form = Edit_case(request.POST)
        if form.is_valid():
            events = form.cleaned_data["event_list"]
            
            for event in events:
                try:
                    event.add_attendee(case)
                except:
                    messages.error(request, "Failed to add case to "+event+"! Date missmatch.")

            return redirect('/case/'+case.case_number)


    form = Edit_case()
    context.update({"form": form})
    context.update({"case": case})


    return HttpResponse(template.render(context,request))