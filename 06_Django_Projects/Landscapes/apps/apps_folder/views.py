from django.shortcuts import render, redirect
import random

def index(request):
    return render(request, 'apps_folder/index.html')

def show(request):
    num = int(request.POST['num'])
    if num > 50 or num <= 0:
        return redirect('/')
    if num < 11:
        img = "apps_folder/snow.jpg"
    elif num > 9 and num < 21:
        img = "apps_folder/desert.jpg"
    elif num > 19 and num < 31:
        img = "apps_folder/forest.jpg"
    elif num > 29 and num < 41:
        img = "apps_folder/vineyard.jpg"
    elif num > 30 and num < 51:
        img = "apps_folder/vineyard.jpg"
    return render(request, 'apps_folder/show.html', {'img':img})
