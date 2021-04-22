from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms

from .models import *


class Homepage(forms.Form):
    date_range = forms.DateField()


class New_location(forms.Form):

    location_name           = forms.CharField(max_length=250, label='Location name'
                                                , widget= forms.TextInput(attrs={'placeholder':'e.g. a restaurant name'}))
    location                = forms.CharField(max_length=250, label='Location'
                                                , widget= forms.TextInput(attrs={'placeholder':'e.g. a building name'}))
    address                 = forms.CharField(max_length=250, label='Address'
                                                , widget= forms.TextInput(attrs={'placeholder':'Don\'t worry, backend will handle this'}))
    date_of_event           = forms.DateField(label='Date of Event'
                                                , widget= forms.TextInput(attrs={'placeholder':'YYYY-mm-dd'}))
    description_of_event    = forms.CharField(max_length=1000, label='Description of event'
                                                , widget= forms.TextInput(attrs={'placeholder':'Briefly describe event'}))
    

    class Meta:
        model   = Location
        fields  = ('location_name', 'location', 'address', 'date_of_event', 'description_of_event')
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add location'))


class New_case(forms.Form):

    case_name       = forms.CharField(max_length=150, label='Name'
                                        , widget= forms.TextInput(attrs={'placeholder':'Enter case name'}))
    case_number     = forms.CharField(max_length=25, label='Case Number'
                                         , widget= forms.TextInput(attrs={'placeholder':'Enter case number'}))
    personal_id     = forms.CharField(max_length=25, label='ID'
                                         , widget= forms.TextInput(attrs={'placeholder':'Enter case personal id'}))
    date_of_birth   = forms.DateField(label='Date of Birth'
                                         , widget= forms.TextInput(attrs={'placeholder':'YYYY-mm-dd'}))
    date_of_onset   = forms.DateField(label='Date of Symptoms Onset'
                                         , widget= forms.TextInput(attrs={'placeholder':'YYYY-mm-dd'}))
    date_of_test    = forms.DateField(label='Date of Positive Test'
                                         , widget= forms.TextInput(attrs={'placeholder':'YYYY-mm-dd'}))
    case_event      = forms.ModelChoiceField(label='Event'
                                         , queryset=Location.objects.all().order_by('name')
                                         , required=False)

    class Meta:
        model   = Case
        fields  = ('case_name', 'case_number', 'personal_id', 'date_of_birth', 'date_of_onset', 'date_of_test', 'case_event')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add case'))