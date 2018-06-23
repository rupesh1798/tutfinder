from django.db.models import Q

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )
from rest_framework.exceptions import NotFound
#from posts.permissions import IsOwnerOrReadOnly
#from posts.pagination import PostLimitOffsetPagination, PostPageNumberPagination
from django.contrib.auth import get_user_model


User = get_user_model()
from .models import Profile
from .permissions import IsOwner
from .serializers import (
    UserLoginSerializer,
    UserCreateSerializer,
    ProfileSerializer,
    )


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    queryset = User.objects.all()


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    # queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data = data)
        if serializer.is_valid(raise_exception = True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ProfileDetailAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [AllowAny]
    lookup_field = 'username'
    #lookup_url_kwrg = 'user'

    def retrieve(self, request, username, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            profile = Profile.objects.select_related('user').get(
                user__username=username
            )
        except Profile.DoesNotExist:
            raise NotFound(detail='Profile not found', code='404 Not Found')

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=HTTP_200_OK)


class ProfileUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]
    lookup_field = 'username'
    #lookup_url_kwrg = 'user'

# class ProfileDeleteAPIView(DestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsOwner]
#     lookup_field = 'slug'
#     # lookup_url_kwrg = 'slug'

