from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^farm',views.farm),
    url(r'^house',views.house),
    url(r'^cave',views.cave),
    url(r'^casino',views.casino),
    url(r'^reset',views.reset),
]
