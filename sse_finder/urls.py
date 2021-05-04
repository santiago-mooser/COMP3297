from django.urls import path

from . import views

urlpatterns = [

      #Redirect default views to HK
    path('', views.homepage, name='homepage'),
    path('home/', views.homepage, name='homepage'),
    path('login/',views.login_view, name="loginpage"),

    #Path to add a new resource
    path('add/location', views.add_location, name='add_location'),
    path('add/case', views.add_case, name='add_case'),

    path('location/<str:loc_name>', views.location_details, name='location_details'),
    path('case/<str:case_num>', views.case_details, name='case_details'),

    path('find/case', views.find_case, name='find_case'),
    path('find/error', views.find_error, name='find_erro'),
]