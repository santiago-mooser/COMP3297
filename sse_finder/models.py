from django.db import models
from django.db.models.deletion import CASCADE

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from requests.models import CaseInsensitiveDict
import requests, datetime, json

class Case(models.Model):

    name            = models.CharField(max_length=150)
    case_number     = models.CharField(max_length=25, unique=True)
    personal_id     = models.CharField(max_length=25, unique=True)
    date_of_birth   = models.DateField()
    date_of_onset   = models.DateField()
    date_of_test    = models.DateField()
    
    def get_details(self):
        details = {
            "case":{
                "name": self.name,
                "case_number": self.case_number,
                "personal_id": self.personal_id,
                "date_of_birth": self.date_of_birth,    
                "date_of_onset": self.date_of_onset,
                "date_of_test":self.date_of_test,
            }
        }

        return details

    def __str__(self):
        return self.name


class Location(models.Model):

    venue_name              = models.CharField(max_length=250, unique=True)
    building_name           = models.CharField(max_length=250)
    coordinate_x            = models.IntegerField(null=True)
    coordinate_y            = models.IntegerField(null=True)
    address                 = models.CharField(max_length=250)
    date_of_event           = models.DateField()
    description_of_event    = models.CharField(max_length=1000)
    attendees               = models.ManyToManyField(Case)

    def __str__(self):
        return self.venue_name

    def add_attendee(self, case):

        if(self.date_of_event > (case.date_of_onset - datetime.timedelta(days=14)) 
        and self.date_of_event< case.date_of_test):
            self.attendees.add(case)
        else:
            try:
                pass
            except:
                raise

    def get_details(self):
        details = {
            "location":{
                "venue_name": self.venue_name,
                "building_name": self.building_name,
                "address": self.address,
                "coordinate_x": self.coordinate_x,
                "coordinate_y": self.coordinate_y,
                "date_of_event": self.date_of_event,
                "description_of_event": self.description_of_event,
                "case_num": self.attendees.count()
            }
        }

        return details


@receiver(pre_save, sender=Location)
def retrieve_coordinates(sender, instance, *args, **kwargs):

    api     = "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch"

    response = requests.get(api, params={"q": instance.building_name})

    details = response.json()[0]

    print(details)

    instance.coordinate_x = details.get("x")
    instance.coordinate_y = details.get("y")
    instance.address = details.get("addressEN")

class CHP_User(models.Model):
    # add field for CHP id number
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_number = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.staff_number
