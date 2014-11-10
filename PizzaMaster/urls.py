from django.conf.urls import patterns, url
from PizzaMaster.app.views import home
urlpatterns = patterns(
    '',
    url(r'^$', home, name='index'),
)
