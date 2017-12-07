from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

def index(request):
    context={
    "all_courses": Course.objects.all()
    }
    return render(request, "main/index.html", context)

def create(request):
    if request.method=="POST":
        response_from_models = Course.objects.validate_course(request.POST)
        if response_from_models["status"]:
            pass
        else:
            for error in response_from_models["errors"]:
                messages.error(request, error)
    return redirect('courses:index')

def delete(request, id):
    Course.objects.delete_course(id)
    return redirect('courses:index')
# Create your views here.
