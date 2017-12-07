from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return render(request, 'index.html')

def result(request):
    return render(request, "survey/success.html")

def success(request):
    if request.method == 'POST':
        print(request.POST)
        context ={
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment']
        }

        return render(request, 'success.html', context)
    else:
        return redirect('/')
