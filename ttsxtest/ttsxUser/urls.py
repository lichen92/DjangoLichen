from  django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/$', views.ttsx_zhuce),
    url(r'^$', views.center),
    url(r'^login/$', views.ttsx_denglud),
    url(r'^loginz/$', views.ttsx_dengluz),
    url(r'^register_valid/$', views.register_valid),
    url(r'^login_handle/$', views.login_handle),
    url(r'^site/$', views.site),
    url(r'^order/$', views.order),
    url(r'^card/$', views.cart),
    url(r'^logout', views.logout),
]

