from  django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/$', views.ttsx_zhuce),
    url(r'^$',views.index),
    url(r'^login/$', views.ttsx_denglud),
    url(r'^loginz/$', views.ttsx_dengluz),
]