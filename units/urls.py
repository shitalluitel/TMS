from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.unit_list, name='unit_list'),
    url(r'^new/$', views.unit_create, name='unit_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.unit_edit, name='unit_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.unit_delete, name='unit_delete'),
]
