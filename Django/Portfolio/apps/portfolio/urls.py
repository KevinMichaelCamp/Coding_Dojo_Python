from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^python$', views.python),
    url(r'^ruby$', views.ruby),
    url(r'^mean$', views.mean)
]