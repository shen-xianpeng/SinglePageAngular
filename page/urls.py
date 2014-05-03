from django.conf.urls import patterns, include, url
import os


from .views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UpFile.views.home', name='home'),
    url(r'^$', index),

 

)
