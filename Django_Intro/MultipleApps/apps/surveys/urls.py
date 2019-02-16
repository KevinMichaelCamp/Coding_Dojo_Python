from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^surveys$', views.surveys, name='surveys'),
    url(r'^surveys/new$', views.new, name='new'),
]
