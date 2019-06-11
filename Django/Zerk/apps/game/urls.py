from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^existing$', views.existing, name='existing'),
    url(r'^home$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^new$', views.new, name='new'),
    url(r'^register$', views.register, name='register'),
]
