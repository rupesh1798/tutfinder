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
    TrackListSerializer,
    TrackDetailSerializer,
    TrackCreateUpdateSerializer,
    TrackDeleteSerializer,

)

from .models import Track

class TrackCreateAPIView(CreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackCreateUpdateSerializer
    permission_classes = [IsAdminUser]

class TrackListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = TrackListSerializer
    filter_backends = [SearchFilter, OrderingFilter] #ordering=title in url (-title gives opposite)
    search_fields = ['title', 'detail']
    # pagination_class = PostPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView,self).get_queryset(*args, **kwargs)
        queryset_list = Track.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(detail__icontains=query)
                ).distinct()
        return queryset_list

class TrackDetailAPIView(RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackDetailSerializer
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class TrackDeleteAPIView(DestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackDeleteSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class TrackUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackCreateUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
    # lookup_url_kwrg = 'slug'

class TrackFeaturedListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = TrackListSerializer
    filter_backends = [SearchFilter, OrderingFilter] #ordering=title in url (-title gives opposite)
    search_fields = ['title', 'detail']
    # pagination_class = PostPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        return Track.objects.filter(featured=True)
