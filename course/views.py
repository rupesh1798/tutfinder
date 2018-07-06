#from rest_framework import status
from django.db.models import Q
#from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response

from rest_framework.generics import (
    GenericAPIView,
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
    CourseListSerializer,
    CourseDetailSerializer,
    CourseCreateUpdateSerializer,
    CourseDeleteSerializer,
    SubmitCourseCreateUpdateSerializer,
)

from .models import Course, SubmitCourse

class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateUpdateSerializer
    permission_classes = [IsAdminUser]
    def perform_create(self, serializer):
        serializer.save(submitter=self.request.user)

class CourseListAPIView(ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = CourseListSerializer
    # permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter] #ordering=title in url (-title gives opposite)
    search_fields = ['title', 'content', 'user__first_name']
    # pagination_class = PostPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView,self).get_queryset(*args, **kwargs)
        queryset_list = Course.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(detail__icontains=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)|
                Q(tech__title__icontains=query)
                ).distinct()
        user = self.request.user
        if user.is_authenticated():
            for obj in queryset_list:
                if user in obj.upvotes.all():
                    obj.upvote_user = True
                else:
                    obj.upvote_user = False
        return queryset_list

class CourseTechListAPIView(ListAPIView):
    serializer_class = CourseListSerializer
    # permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]  # ordering=title in url (-title gives opposite)
    search_fields = ['title', 'content', 'user__first_name']
    # pagination_class = PostPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        tech_slug = self.kwargs['tech_slug']
        return Course.objects.filter(tech__slug = tech_slug)


class CourseUserListAPIView(ListAPIView):
    serializer_class = CourseListSerializer
    # permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]  # ordering=title in url (-title gives opposite)
    search_fields = ['title', 'content', 'user__first_name']
    # pagination_class = PostPageNumberPagination
    def get_queryset(self, *args, **kwargs):
        user = self.kwargs['user']
        return Course.objects.filter(submitter__username = user)

class CourseDetailAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    # permission_classes = [AllowAny]
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class CourseDeleteAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDeleteSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    # lookup_url_kwrg = 'slug'

class CourseUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    permission_classes = [IsAdminUser]
    # lookup_url_kwrg = 'slug'

class SubmitCourseCreateAPIView(CreateAPIView):
    queryset = SubmitCourse.objects.all()
    serializer_class = SubmitCourseCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CourseUpvoteAPIToggle(GenericAPIView):
    #authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = [IsAuthenticated]

    def get(self, request, slug=None, format=None):
        # slug = self.kwargs.get("slug")
        obj = get_object_or_404(Course, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        voted = False
        if user.is_authenticated():
            if user in obj.upvotes.all():
                voted = False
                obj.upvotes.remove(user)
            else:
                voted = True
                obj.upvotes.add(user)
            updated = True
        data = {
            "updated": updated,
            "voted": voted,
        }
        return Response(data)