from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^addme/(?P<id>\d+)$', views.addme),
    url(r'^dashboard$', views.dashboard),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^create$', views.create),
    url(r'^register$', views.register),
    url(r'^remove/(?P<id>\d+)$', views.remove),
]
