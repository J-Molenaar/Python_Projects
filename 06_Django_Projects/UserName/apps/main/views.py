from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

def index(request):
    context={
    "all_users"= Users.objects.all()
    }
    return render(request, "main/index.html", context)

def create(request):
    if request.method="POST":
        response_from_models = User.objects.user_validation(request.POST)
        if response_from_models['status']:
            pass
        else:
            for error in response_from_models['errors']:
                messages.error(request, error)
    return redirect('users:index')
# Create your views here.
