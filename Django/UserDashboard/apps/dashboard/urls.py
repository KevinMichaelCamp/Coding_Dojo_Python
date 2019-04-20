from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^login$', views.login, name='login'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'^register$', views.register, name='register'),
    url(r'^admin_dashboard$', views.admin_dashboard, name='admin_dashboard'),
    url(r'^user_dashboard$', views.user_dashboard, name='user_dashboard'),
    url(r'^user_edit$', views.user_edit, name='user_edit'),
    url(r'^edit_info', views.edit_info, name='edit_info'),
    url(r'^edit_password', views.edit_password, name='edit_password'),
    url(r'^admin_edit/(?P<id>\d+)', views.admin_edit, name='admin_edit'),
    url(r'^admin_edit_info/(?P<id>\d+)', views.admin_edit_info, name='admin_edit_info'),
    url(r'^admin_edit_password/(?P<id>\d+)', views.admin_edit_password, name='admin_edit_password'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^add$', views.add, name='add'),
    url(r'^admin_add$', views.admin_add, name='admin_add'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^message/(?P<id>\d+)$', views.message, name='message'),
    url(r'^logout$', views.logout, name='logout'),
]
