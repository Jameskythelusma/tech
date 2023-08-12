from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'techfest2023.html')

def apply(request):
    return render(request,'apply.html')