from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blogs$', views.index, name='blogs'),
    url(r'^blogs/new$', views.new, name='new'),
    url(r'^blogs/create$', views.create, name='create'),
    url(r'^blogs/(?P<number>\d+)$', views.show, name='show'),
    url(r'^blogs/(?P<number>\d+)/edit$', views.edit, name='edit'),
    url(r'^blogs/(?P<number>\d+)/delete$', views.delete, name='delete'),
]
