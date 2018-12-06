from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'outra_view/',views.outra_view, name = 'outra_view'),
        )