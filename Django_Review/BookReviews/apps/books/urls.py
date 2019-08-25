from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books$', views.books),
    url(r'^books/add$', views.add),
    url(r'^books/create$', views.create),
    url(r'^books/(?P<id>\d+)$', views.display),
    url(r'^books/add_review/(?P<id>\d+)$', views.review),
    url(r'^users/(?P<id>\d+)$', views.user),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]
