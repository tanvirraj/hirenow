from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import renderers
from userprofile import views
from userprofile.views import *


urlpatterns = [
    # api
    url(r'^user/$', UserProfileList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', UserProfileDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)