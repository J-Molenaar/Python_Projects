from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'index.html')

def show(request):
    return render(request, 'testimonials.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')
