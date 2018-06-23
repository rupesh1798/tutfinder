from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    ProfileDetailAPIView,
    ProfileUpdateAPIView,

    )

urlpatterns = [
    url(r'^register$', UserCreateAPIView.as_view(), name='register'),
    url(r'^login$', UserLoginAPIView.as_view(), name='login'),
    url(r'^profile/(?P<username>[\w-]+)/$', ProfileDetailAPIView.as_view(), name='profile_detail'),
    url(r'^profile/(?P<username>[\w-]+)/edit/$', ProfileUpdateAPIView.as_view(), name='profile_update'),

]
