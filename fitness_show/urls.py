from django.conf.urls import patterns, url
from fitness_show import views

urlpatterns = patterns('',
                       url(r'^$', views.show, name='show'),
                       )
