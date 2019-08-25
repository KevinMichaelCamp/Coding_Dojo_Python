from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^home$', views.home),
    url(r'^friend/(?P<id>\d+)$', views.friend),
    url(r'^unfriend/(?P<id>\d+)$', views.unfriend),
]
