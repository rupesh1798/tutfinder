from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    TrackListAPIView,
    TrackDetailAPIView,
    TrackCreateAPIView,
    TrackUpdateAPIView,
    TrackDeleteAPIView,
    TrackFeaturedListAPIView,
)


urlpatterns = [
    url(r'^$', TrackListAPIView.as_view(), name='track_list'),
    url(r'^create/$', TrackCreateAPIView.as_view(), name='track_create'),
    url(r'^(?P<slug>[\w-]+)/$', TrackDetailAPIView.as_view(), name='track_detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', TrackUpdateAPIView.as_view(), name='track_update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', TrackDeleteAPIView.as_view(), name='track_delete'),
    # url(r'^posts/$', "<appname>.views.<function_name>"),
    url(r'^featured/$', TrackFeaturedListAPIView.as_view(), name='track_featured_list'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
