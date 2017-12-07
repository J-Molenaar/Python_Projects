from django.shortcuts import render, redirect, HttpResponse
from .models import Book
from django.contrib import messages
def index(request):
    context={
    "all_books": Book.objects.all()
    }
    return render(request, 'main/index.html', context)

def create(request):
    if request.method=='POST':
        response_from_models = Book.objects.validate_book(request.POST) #this line triggers the validate_book in models to run.

        if response_from_models['status']:
            pass
        else:
            for error in response_from_models['errors']:
                messages.error(request, error)
    return redirect("books:index")



# (title=request.POST["title"], author=request.POST["author"], category=request.POST["category"])
