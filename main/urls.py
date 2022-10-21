from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('greeting/', views.greeting, name='greeting'),
    path('facility/', views.facility, name='facility'),
    path('history/', views.history, name='history'),
    path('contact/', views.contact, name='contact'),
    path('masters/', views.masters, name='masters'),
]