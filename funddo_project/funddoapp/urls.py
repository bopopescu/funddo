from django.conf.urls import patterns, url
from funddoapp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	)