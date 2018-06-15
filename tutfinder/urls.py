from django.conf.urls import url, include
from django.contrib import admin
from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import views, serializers, status
from rest_framework.response import Response
class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()

class EchoView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)

urlpatterns = [
    url(r'^$', generic.RedirectView.as_view(
         url='/api/', permanent=False)),
    url(r'^api/$', get_schema_view()),
    url(r'^api/auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/token/obtain/$', TokenObtainPairView.as_view()),
    url(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),
    url(r'^admin/', admin.site.urls),
    #url(r'', include('core.urls')),
    url(r'^api/technology/', include("technology.urls", namespace='tech')),
    url(r'^api/', include("course.urls", namespace='course')),
    url(r'^api/track/', include("track.urls", namespace='track')),
    url(r'^api/', include("track_course.urls", namespace='track_course')),
#    url(r'', include('user.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api/echo/$', EchoView.as_view())
]
