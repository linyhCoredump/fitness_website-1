from django.conf.urls import patterns, url
from fitness_app import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^userlogin', views.userlogin, name='userlogin'),
                       url(r'^sub', views.sub, name='sub'),
                       url(r'^register/', views.register, name='register'),
                       )
