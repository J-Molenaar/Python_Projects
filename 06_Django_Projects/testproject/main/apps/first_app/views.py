#CONTROLLER
from django.shortcuts import render, HttpResponse
def index(request):
    print "*" * 10
    response = "HEllO, I am your first request!"
    return render(request, "first_app/index.html")
# Create your views here.

def show(request):
    return render(request, "first_app/users.html")
