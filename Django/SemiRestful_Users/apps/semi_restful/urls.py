from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^validate$', views.validate, name='validate'),
    url(r'^revalidate/(?P<id>\d+)$', views.revalidate, name='revalidate'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^clear$', views.clear, name='clear'),
]
