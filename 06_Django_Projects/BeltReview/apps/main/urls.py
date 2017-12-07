from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^/post$', views.post),
    # url(r'^logout$', views.logout),
    # url(r'^like/(?P<id>\d+)$', views.add_like, name='add_like'),
    # url(r'^top10$', views.top10, name='top10'),
    # url(r'^delete/(?P<id>\d+)$', views.delete, name='delete')
]
