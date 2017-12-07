from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^success$', views.success, name='sucess'),
    url(r'^result$', views.result, name = "result")
]
