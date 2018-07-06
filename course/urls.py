from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    CourseCreateAPIView,
    CourseListAPIView,
    CourseTechListAPIView,
    CourseUserListAPIView,
    CourseDetailAPIView,
    CourseDeleteAPIView,
    CourseUpdateAPIView,
    SubmitCourseCreateAPIView,
    CourseUpvoteAPIToggle,
)

urlpatterns = [
    url(r'^course/$', CourseListAPIView.as_view(), name='course_list'),
    url(r'^courses/(?P<tech_slug>[\w-]+)/$', CourseTechListAPIView.as_view(), name='course_tech_list'),
    url(r'^courses/user/(?P<user>[\w-]+)/$', CourseUserListAPIView.as_view(), name='course_user_list'),
    url(r'^course/create/$', CourseCreateAPIView.as_view(), name='course_create'),
    url(r'^course/(?P<slug>[\w-]+)/$', CourseDetailAPIView.as_view(), name='course_detail'),
    url(r'^course/(?P<slug>[\w-]+)/edit/$', CourseUpdateAPIView.as_view(), name='course_update'),
    url(r'^course/(?P<slug>[\w-]+)/delete/$', CourseDeleteAPIView.as_view(), name='course_delete'),
    url(r'^course/submit/$', SubmitCourseCreateAPIView.as_view(), name='course_submit'),
    url(r'^course/(?P<slug>[\w-]+)/upvote/$', CourseUpvoteAPIToggle.as_view(), name='Upvote-api-toggle'),
    # url(r'^posts/$', "<appname>.views.<function_name>"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
