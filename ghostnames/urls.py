from django.conf.urls.defaults import *
from ghostnames.views import choose_ghost_name, list_names,confirm_ghost_name
from django.conf.urls import url


urlpatterns = patterns('ghostnames.views',
    url(r'^choose/(?P<uid>\d+)', choose_ghost_name, name='choose'),
    url(r'^choose', choose_ghost_name),
    url(r'^confirm/(?P<uid>\d+)', confirm_ghost_name, name='confirm'),
    url(r'^$', list_names, name='home'),
)