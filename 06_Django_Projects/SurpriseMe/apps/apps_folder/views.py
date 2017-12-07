from django.shortcuts import render, redirect
import random

values = ['Marshmallow', 'Trash Panda', 'Gingerbread', 'Bad Kitty', 'Gummi Bears']

def index(request):
    return render(request, 'apps_folder/index.html')

def show(request):
    request.session['num'] = request.POST['num']
    return redirect('/results')

def results(request):
    random.shuffle(values)
    request.session.items = values[0:int(request.session['num'])] #everything in session is always a string. If int required, typecast with int()
    return render(request, 'apps_folder/show.html')
