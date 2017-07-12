from django.conf.urls import url
from . import views
from views import MySearchView


urlpatterns = [
    url(r'^$', views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list),
    url(r'^detail(\d+)/$', views.detail),
    url(r'^search/?$', MySearchView.as_view(), name='search_view'),
]