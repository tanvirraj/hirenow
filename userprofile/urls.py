from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import renderers
from userprofile import views
from userprofile.views import *


urlpatterns = [
    # api
    url(r'^userprofile/$', UserProfileList.as_view()),
    url(r'^userprofiledetail/(?P<pk>[0-9]+)/$', UserProfileDetail.as_view()),
    url(r'^user/$', UserList.as_view()),
    url(r'^userdetail/(?P<pk>[0-9]+)/$', UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)