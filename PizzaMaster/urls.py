from django.conf.urls import patterns, url
from PizzaMaster.app.views import home
from django.conf import settings
urlpatterns = patterns(
    '',
    url(r'^$', home, name='index'),
)

urlpatterns += patterns('',
    (r'^static/(?P.*)\$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
