from django.conf.urls.defaults import *
from ghostnames.views import choose_ghost_name, list_names,confirm_ghost_name, suggestioned_names_api, register_nickname,names_api
from django.conf.urls import url


urlpatterns = patterns('ghostnames.views',
                       url(r'^choose/(?P<uid>\d+)', choose_ghost_name, name='choose'),
                       url(r'^choose', choose_ghost_name),
                       url(r'^confirm/(?P<uid>\d+)', confirm_ghost_name, name='confirm'),
                       url(r'^suggestioned_names_api/', suggestioned_names_api, name='suggestioned_names_api'),
                       url(r'^api/register/', register_nickname, name='register_nickname_api'),
                       url(r'^api/names_api/', names_api, name='names_api'),
                       url(r'^$', list_names, name='home'),
                       )