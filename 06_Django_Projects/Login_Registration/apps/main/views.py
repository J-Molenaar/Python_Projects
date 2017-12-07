from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

def index(request):
    return render(request, "main/index.html")

def success(request):

    return render(request, 'main/success.html')

def register(request):
    if request.method=="POST":
        response_from_models = User.objects.user_validation(request.POST)
        if response_from_models['status']:
            request.session["first_name"] = response_from_models['user'].first_name
            pass
        else:
            request.session['error_group'] = True
            for i in response_from_models["error"]:
                messages.error(request, i)
            return redirect('/')
    else:
        return redirect('/')

    return redirect('/success')

def login(request):
    if request.method=="POST":
        response_from_models = User.objects.login_validation(request.POST)
        if response_from_models['status']:
            request.session["first_name"] = response_from_models['user'].first_name
            pass
        else:
            request.session['error_group'] = False
            for i in response_from_models["errors"]:
                messages.error(request, i)
            return redirect('/')
    else:
        return redirect('/')

    return redirect('/success')
# Create your views here.
