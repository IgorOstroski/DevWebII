from django.conf.urls import include, url
from son_of_blah import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
