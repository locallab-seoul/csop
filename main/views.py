from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def greeting(request):
    return render(request, 'greeting.html')

def facility(request):
    return render(request, 'facility.html')

def history(request):
    return render(request, 'history.html')

def contact(request):
    return render(request, 'contact.html')

def masters(request):
    return render(request, 'masters.html')