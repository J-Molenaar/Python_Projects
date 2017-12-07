from django.shortcuts import render, redirect, HttpResponse
import datetime
from django.utils import timezone

def index(request):
    now = timezone.now()
    context = {
        'time' : datetime.datetime.now()
    }
    return render(request, 'index.html', context)
