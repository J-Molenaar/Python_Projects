from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def show(request):
    return render(request, 'testimonials.html')
