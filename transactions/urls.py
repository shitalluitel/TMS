from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.transaction_create, name='home_page'),
    url(r'^transactions/$', views.transaction_list, name='transaction_list'),
    url(r'^transactions/new/$', views.transaction_create, name='transaction_create'),
    url(r'^transactions/(?P<pk>\d+)/edit/$', views.transaction_edit, name='transaction_edit'),
    # url(r'^(?P<pk>\d+)/delete/$', views.transaction_delete, name='transaction_delete'),
]
