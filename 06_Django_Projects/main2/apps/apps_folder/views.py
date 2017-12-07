from django.shortcuts import render

def index(request):
    context = {
        'email': "me@me.com",
        'name': "Jessica"
    }
    return render(request, 'apps_folder/index.html', context)

def show(request, id):
    context = {
        'id': id
    }
    return render(request, 'apps_folder/show.html', context)
# Create your views here.
