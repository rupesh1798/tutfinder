#from rest_framework import status
from django.db.models import Q
#from django.contrib.auth.models import User
#from django.shortcuts import render
#from rest_framework.response import Response

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from .serializers import (
    TrackCourseListSerializer,
    TrackCourseDetailSerializer,
    TrackCourseCreateUpdateSerializer,
    TrackCourseDeleteSerializer,
)

from .models import TrackCourse

class TrackCourseCreateAPIView(CreateAPIView):
    queryset = TrackCourse.objects.all()
    serializer_class = TrackCourseCreateUpdateSerializer
    permission_classes = [IsAdminUser]
    def perform_create(self, serializer):
        serializer.save(submitter=self.request.user)

class TrackCourseListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = TrackCourseListSerializer
    filter_backends = [SearchFilter, OrderingFilter] #ordering=title in url (-title gives opposite)
    search_fields = ['title', 'detail']
    # pagination_class = PostPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView,self).get_queryset(*args, **kwargs)
        queryset_list = TrackCourse.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(detail__icontains=query)|
                Q(track__title__icontains=query)
                ).distinct()
        return queryset_list

class TrackCourseFilteredListAPIView(ListAPIView):
    serializer_class = TrackCourseListSerializer
    filter_backends = [SearchFilter, OrderingFilter]  # ordering=title in url (-title gives opposite)
    search_fields = ['title', 'detail']
    # pagination_class = PostPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        track_slug = self.kwargs['track_slug']
        return TrackCourse.objects.filter(track__slug = track_slug)

class TrackCourseDetailAPIView(RetrieveAPIView):
    queryset = TrackCourse.objects.all()
    serializer_class = TrackCourseDetailSerializer
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class TrackCourseDeleteAPIView(DestroyAPIView):
    queryset = TrackCourse.objects.all()
    serializer_class = TrackCourseDeleteSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class TrackCourseUpdateAPIView(RetrieveUpdateAPIView):
    queryset = TrackCourse.objects.all()
    serializer_class = TrackCourseCreateUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'
