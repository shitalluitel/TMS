from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^new/$', views.item_create, name='item_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.item_delete, name='item_delete'),
    url(r'^(?P<pk>\d+)/get/unit_price/$', views.item_unit_price, name='item_unit_price'),
]
