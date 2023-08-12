from django.urls import path
from techfest.views import apply,home

urlpatterns = [
    path('',home,name='home'),
    path('apply/',apply,name='Apply'),
   
]