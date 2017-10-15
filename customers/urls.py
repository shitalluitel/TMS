from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.customer_create, name='customer_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.customer_edit, name='customer_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.customer_delete, name='customer_delete'),
    url(r'^(?P<pk>\d+)/trash/$', views.customer_soft_delete, name='customer_soft_delete'),
    url(r'^(?P<pk>\d+)/restore/$', views.customer_restore, name='customer_restore'),
    url(r'^list/$', views.customer_list, name='customer_list')
]
