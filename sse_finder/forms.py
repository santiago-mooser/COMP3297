from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'



class Homepage(forms.Form):
    date_from_range = forms.DateTimeField(label = '', widget=DateInput)
    date_to_range = forms.DateTimeField(label = '', widget=DateInput)



class New_location(forms.Form):

    venue_name = forms.CharField(
                            max_length=250,
                            label='Venue name',
                            widget= forms.TextInput(attrs={
                                    'placeholder':'e.g. a restaurant name'}))
    
    building_name = forms.CharField(
                            max_length=250,
                            label='Building name',
                            widget= forms.TextInput(attrs={
                                    'placeholder':'e.g. a building name'}))
    
    date_of_event = forms.DateField(
                            label='Date of Event',
                            widget=DateInput)

    description_of_event = forms.CharField(
                            max_length=1000,
                            label='Description of event',
                            widget= forms.Textarea(attrs={
                                        'placeholder':'Briefly describe event',
                                        'rows':4,
                                        'cols': 40}))
    

    class Meta:
        model   = Location
        fields  = (
                'venue_name',
                'building_name',
                'address',
                'date_of_event',
                'description_of_event')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add location'))



class New_case(forms.Form):

    case_name = forms.CharField(
                            max_length=150,
                            label='Name',
                            widget= forms.TextInput(attrs={
                                    'placeholder':'Case Name'}))
                                    
    case_number = forms.CharField(
                            max_length=25,
                            label='Case Number',
                            widget= forms.TextInput(attrs={
                                    'placeholder':'Case Number'}))

    personal_id = forms.CharField(
                            max_length=25,
                            label='ID',
                            widget= forms.TextInput(attrs={
                                    'placeholder':'Personal ID'}))
    
    date_of_birth = forms.DateField(
                            label='Date of Birth',
                            widget=DateInput)

    date_of_onset = forms.DateField(
                            label='Date of Symptoms Onset',
                            widget=DateInput)

    date_of_test = forms.DateField(
                            label='Date of Positive Test',
                            widget=DateInput)

    case_event = forms.ModelMultipleChoiceField(
                        label='Event',
                        queryset=Location.objects.all().order_by('venue_name'),
                        widget=forms.CheckboxSelectMultiple(),
                        required=False)


    class Meta:
        model   = Case
        fields  = (
                'case_name',
                'case_number',
                'personal_id',
                'date_of_birth',
                'date_of_onset',
                'date_of_test',
                'case_event')
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add case'))



class Find_case(forms.Form):
    case_number     = forms.CharField(max_length=25, label='What is the Case Number?'
                                         , widget= forms.TextInput(attrs={'placeholder':'Enter case number'}))
    # TODO: Data validation
    # def clean(self):
    #     cleaned_data = super().clean()
    #     case_number = cleaned_data.get("case_number")

    #     if not isinstance(case_number)



class Edit_case(forms.Form):

    event_list = forms.ModelMultipleChoiceField(
                            label='Event',
                            queryset=Location.objects.all().order_by('venue_name'),
                            widget=forms.CheckboxSelectMultiple(),
                            required=False)

    class Meta:
        fields  = (
                'event_list',
                )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add event'))