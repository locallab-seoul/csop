from tkinter.messagebox import NO
from django.shortcuts import render
from .models import Notice

# Create your views here.

def board_list(request):
    all_boards  = Notice.objects.all().order_by('-id')
    return render(request, 'board-list.html', {'notices': all_boards})