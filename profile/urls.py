from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserDetailAPIView,
    ChangePasswordAPIView,
    ProfileDetailAPIView,
    ProfileUpdateAPIView,
    #FacebookLogin,

    )

urlpatterns = [
    #url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    #url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    #url(r'^change_password/$', ChangePasswordAPIView.as_view(), name='change_password'),
    #url(r'^detail/$', UserDetailAPIView.as_view(), name='detail'),

    url(r'^profile/(?P<username>[\w-]+)/$', ProfileDetailAPIView.as_view(), name='profile_detail'),
    url(r'^profile/(?P<user__username>[\w-]+)/edit/$', ProfileUpdateAPIView.as_view(), name='profile_update'),
    #url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login')


]
