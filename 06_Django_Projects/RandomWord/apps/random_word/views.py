from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
	if 'count' not in request.session:
		request.session['count'] = 0
	else:
		request.session['word'] = get_random_string(length=14)
	return render(request, "index.html")

def generate(request):
	if request.method == 'POST':
		request.session['count'] += 1
	return redirect('/')
# Create your views here.
