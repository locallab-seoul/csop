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
    path('master-cristina/', views.master_cristina, name='master-cristina'),
    path('master-gavin/', views.master_gavin, name='master-gavin'),
    path('master-kimtaeyong/', views.master_kimtaeyong, name='master-kimtaeyong'),
    path('master-lina/', views.master_lina, name='master-lina'),
    path('master-michael/', views.master_michael, name='master-michael'),
    path('master-stephen/', views.master_stephen, name='master-stephen'),
    path('master-yoonjungsub/', views.master_yoonjungsub, name='master-yoonjungsub'),
    
    path('program-2022-autumn/', views.program_2022_autumn, name='program-2022-autumn'),
    path('program-2021-spring/', views.program_2023_spring, name='program-2023-spring'),
    path('program-regular/', views.program_regular, name='program-regular'),
]