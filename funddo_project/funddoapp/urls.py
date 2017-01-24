from django.conf.urls import patterns, url
from funddoapp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^make_request/', views.make_request, name ='make_request'),
	url(r'^register/', views.register, name='register'),
	url(r'^login/', views.user_login, name='login'),
	url(r'^logout/', views.user_logout, name='logout'),
	url(r'^about/', views.about, name='about'),
	url(r'^requests/(?P<requests_id>[\W\-]+)/$', views.requests, name='request'),
	)