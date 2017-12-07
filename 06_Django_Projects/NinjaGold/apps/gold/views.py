from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    print ('$' * 100)
    if not 'activity' in request.session:
        request.session['activity'] = []
    print ("!" * 20)
    return render(request, "gold/index.html")

def farm(request):
    reward = random.randrange(10,20)
    request.session['gold'] += reward
    request.session['activity'].append('You won ' + str(reward) + ' gold coins at cave. ' + (str(datetime.datetime.now())))
    return redirect("/")

def cave (request):
    reward = random.randrange(5,10)
    request.session['gold'] += reward
    request.session['activity'].append('You won ' + str(reward) + ' gold coins at farm. ' + (str(datetime.datetime.now())))
    return redirect("/")

def house(request):
    reward = random.randrange(2,5)
    request.session['gold'] += reward
    request.session['activity'].append('You won ' + str(reward) + ' gold coins at house. ' + (str(datetime.datetime.now())))
    return redirect("/")

def casino(request):
    reward = random.randrange(0,50)
    i = random.randrange(1,3)
    if i == 1:
        request.session['gold'] += reward
        request.session['activity'].append('Entered a casino and won ' + str(reward) + ' gold coins. ' + (str(datetime.datetime.now())))
    else:
        request.session['gold'] -= reward
        request.session['activity'].append('Entered a casino and lost ' + str(reward) + ' gold coins. Better luck next time. ' + (str(datetime.datetime.now())))
    return redirect("/")

def reset(request):
    del request.session['gold']
    del request.session['activity']
    return redirect("/")
