from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from ..login.models import User
# from .models import << MODEL NAMES HERE>>
from django.contrib import messages
from django.db.models import Count

def index(request):
    return render(request, "main/index.html")
