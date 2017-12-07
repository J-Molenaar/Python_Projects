from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from ..login.models import User
from .models import Secrets, Likes
from django.contrib import messages
from django.db.models import Count

def index(request):
    request.session['top10'] = False
    context = {
    "secrets":Secrets.objects.all().order_by("created_at"),
    'likes':Likes.objects.all(),
    "liked_secrets": Secrets.objects.filter(all_likes__user=request.session["id"])
    }
    return render(request, "secrets/index.html", context)

def post(request):
    if request.method == "POST":
        secret={
            "secret": request.POST["content"],
            "user": User.objects.get(id=request.session["id"])
        }
        response_from_models = Secrets.objects.secrets_validation(secret)
        if response_from_models['status']:
            pass
        else:
            for i in response_from_models["errors"]:
                messages.error(request, i)
                return redirect("secrets:index")
        return redirect("secrets:index")

def add_like(request, id):
    if request.session['id']:
        data = {
        'user_id': request.session['id'],
        'secret_id': id
        }
        response_to_models = Likes.objects.add_like(data)
    else:
        messages.error(request, "Sorry, you are not logged in...")
    if request.session['top10']:
        request.session['top10'] = False
        return redirect("secrets:top10")
    else:
        return redirect("secrets:index")

def top10(request):
    request.session['top10'] = True
    if request.session['id']:
        context = {
        "secrets":Secrets.objects.annotate(top_liked = Count("all_likes")).order_by('-top_liked')[:10],
        "liked_secrets": Secrets.objects.filter(all_likes__user=request.session["id"])
        }
    else:
        messages.error(request, "Sorry, you are not logged in...")
        return redirect("login:index")
    return render(request, "secrets/top10.html", context)

def delete(request, id):
    Secrets.objects.get(id=id).delete()
    if request.session['top10']:
        request.session['top10'] = False
        return redirect("secrets:top10")
    else:
        return redirect("secrets:index")

def logout(request):
    request.session.flush()
    return redirect('login:index')
