from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'fitness_website.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^fitness_app/', include('fitness_app.urls')),
                       url(r'^fitness_show/', include('fitness_show.urls')),
                       )
