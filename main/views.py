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

def master_cristina(request):
    return render(request, 'masters/master-cristina.html')

def master_gavin(request):
    return render(request, 'masters/master-gavin.html')

def master_kimtaeyong(request):
    return render(request, 'masters/master-kimtaeyong.html')

def master_lina(request):
    return render(request, 'masters/master-lina.html')

def master_michael(request):
    return render(request, 'masters/master-michael.html')

def master_stephen(request):
    return render(request, 'masters/master-stephen.html')

def master_yoonjungsub(request):
    return render(request, 'masters/master-yoonjungsub.html')