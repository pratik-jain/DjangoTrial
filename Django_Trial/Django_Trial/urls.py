"""
Definition of urls for Django_Trial.
"""

from django.conf.urls import include, url
import MyApp1.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', MyApp1.views.index, name='index'),
    url(r'^home$', MyApp1.views.index, name='home'),
     
     
     #url(r'^Django_Trial/', include('Django_Trial.Django_Trial.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
