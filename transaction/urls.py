from django.conf.urls import url

from . import views

app_name = 'transaction'
urlpatterns = [
    url(r'^(?P<trans_id>[0-9]+)/$', views.index, name='index'),
]
