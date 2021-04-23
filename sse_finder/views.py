from django.http.response import HttpResponse
from django.template import loader
from django.contrib import messages
from .models import *
from .forms import *
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

    template = loader.get_template('pages/location_details.html')
    context = {}
    
    # we assume that there's only 1 location with the same name. Specified in Project req doc I think

    location    = Location.objects.filter(name = loc_name)[0] 
    cases       = Case.objects.filter(event__name__contains = loc_name)
    
    context.update({'location': location, 'cases': cases})

    return HttpResponse(template.render(context, request))

    try:
        location = Location.objects.get(location_name=loc_name)
    except:
        messages.error(request, "Location not found!")
        return HttpResponse(template.render(context, request))

    context.update(location.get_details())

    return HttpResponse(template.render(context, request))


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