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
    TechnologyListSerializer,
    TechnologyDetailSerializer,
    TechnologyCreateUpdateSerializer,
    TechnologyDeleteSerializer,
)
from .models import Technology


class TechnologyCreateAPIView(CreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologyCreateUpdateSerializer
    permission_classes = [IsAdminUser]

class TechnologyListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = TechnologyListSerializer
    # permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter] #ordering=title in url (-title gives opposite)
    search_fields = ['title', 'detail', 'user__first_name']
    # pagination_class = PostPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView,self).get_queryset(*args, **kwargs)
        queryset_list = Technology.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(detail__icontains=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
                ).distinct()
        return queryset_list

class TechnologyDetailAPIView(RetrieveAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologyDetailSerializer
    # permission_classes = [AllowAny]
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class TechnologyDeleteAPIView(DestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologyDeleteSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class TechnologyUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologyCreateUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
    # lookup_url_kwrg = 'slug'
