from django.conf.urls.defaults import *
from ghostnames.views import choose_ghost_name
from django.conf.urls import url


urlpatterns = patterns('ghostnames.views',
    url(r'^choose', choose_ghost_name, name='choose'),
    (r'^$', 'list_names'),
)