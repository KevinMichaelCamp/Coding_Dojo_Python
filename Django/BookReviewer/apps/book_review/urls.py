from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^books$', views.books, name='books'),
    url(r'^home$', views.home, name='home'),
    url(r'^new_book$', views.new_book, name='new_book'),
    url(r'^library$', views.library, name='library'),
    url(r'^add$', views.add, name='add'),
    url(r'^add_review$', views.add_review, name='add_review'),
    url(r'^display/(?P<id>\d+)$', views.display, name='display'),
    url(r'^user_reviews/(?P<id>\d+)$', views.user_reviews, name='user_reviews'),
    url(r'^logout$', views.logout, name='logout'),
]
