from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from PizzaMaster.app.views import home
urlpatterns = patterns(
    '',
    url(r'^$', home, name='index'),
    # url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
)
