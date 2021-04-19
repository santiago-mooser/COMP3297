from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms.fields import DateField

from .models import *


class Homepage(forms.Form):
    date_range = forms.DateField()


class New_location(forms.Form):

    name                    = forms.CharField(max_length=250, label="Name")
    location                = forms.CharField(max_length=250, label="Location")
    address                 = forms.CharField(max_length=250, label="Address")
    date_of_event           = forms.DateField(label="Date of Event")
    description_of_event    = forms.CharField(max_length=1000, label="Description of event")
    

    class Meta:
        model = Location
        fields = ('name', 'location', 'address', 'date_of_event', 'description_of_event')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add location'))


class New_case(forms.Form):


    name            = models.CharField(max_length=150, label="Name")
    case_number     = models.CharField(max_length=25, unique=True, label="Case Number")
    id              = models.CharField(max_length=25, unique=True, label="ID")
    date_of_birth   = models.DateField(label="Date of Birth")
    date_of_onset   = models.DateField(label="Date of Symptoms Onset")
    date_of_test    = models.DateField(label="Date of Positive Test")



    class Meta:
        model = Location
        fields = ('name', 'case_number', 'id', 'date_of_birth', 'date_of_onset', 'date_of_test')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add case'))