__author__ = 'tanvir'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import renderers
from rides import views
from rides.views import *


urlpatterns = [
    # api
    url(r'^taxilocation/$', TaxiLocationList.as_view()),
    url(r'^taxilocationdetail/(?P<pk>[0-9]+)/$', TaxiLocationDetail.as_view()),

    url(r'^taxisearch/$', TaxiSearchList.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)