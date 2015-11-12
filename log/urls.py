from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^accounts/profile/$', views.profile),
	url(r'^add/$', views.search_game),
	url(r'^add/(?P<gbid>[0-9]+)/$', views.add_game),
]