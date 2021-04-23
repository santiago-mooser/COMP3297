from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Location(models.Model):
    
    name                    = models.CharField(max_length=250)
    location                = models.CharField(max_length=250)
    address                 = models.CharField(max_length=250)
    date_of_event           = models.DateField()
    description_of_event    = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.location_name

class Case(models.Model):

    name            = models.CharField(max_length=150)
    case_number     = models.CharField(max_length=25, unique=True)
    personal_id     = models.CharField(max_length=25, unique=True)
    date_of_birth   = models.DateField()
    date_of_onset   = models.DateField()
    date_of_test    = models.DateField()
    event           = models.ForeignKey(Location, on_delete=models.CASCADE)


    def get_details(self):
        details = {
            "name": self.name,
            "case_number": self.case_number,
            "personal_id": self.personal_id,
            "date_of_birth": self.date_of_birth,    
            "date_of_onset": self.date_of_onset,
            "date_of_test":self.date_of_test,
            "event":self.event,
        }

        return details

    def __str__(self):
        return self.name