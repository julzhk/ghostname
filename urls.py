from django.conf.urls.defaults import *
from django.views.generic.base import RedirectView

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^$', RedirectView.as_view(url='/ghostnames/')),
    (r'^ghostnames/', include('ghostnames.urls')),
)
