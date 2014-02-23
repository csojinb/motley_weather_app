from django.conf.urls import patterns, url

from current_conditions import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)