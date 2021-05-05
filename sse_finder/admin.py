from django.contrib import admin
from .models import Case, Location, CHP_User

# Register your models here.
admin.site.register(Case)
admin.site.register(Location)
admin.site.register(CHP_User)
