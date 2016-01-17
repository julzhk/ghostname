from django.conf.urls.defaults import *

urlpatterns = patterns('ghostnames.views',
    (r'^$', 'list_names'),
)