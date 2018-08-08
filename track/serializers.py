from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from .models import Track
# from django.contrib.auth.models import User

track_detail_url = HyperlinkedIdentityField(
    view_name = 'track:track_detail', #related name in urls
    lookup_field = 'slug'
)

class TrackCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = [
            'title',
            'detail',
            'mentor',
            'time',
            'level',
            'course_count',
            'featured',
        ]

class TrackListSerializer(ModelSerializer):
    url = track_detail_url
    class Meta:
        model = Track
        fields = [
            'id',
            'url',
            'title',
            'slug',
            'detail',
            'mentor',
            'time',
            'level',
            'course_count',
            'featured',
        ]

class TrackDetailSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = [
            'id',
            'title',
            'slug',
            'detail',
            'mentor',
            'time',
            'level',
            'course_count',
            'featured',
        ]

class TrackDeleteSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = [
            'id',
            'url',
            'title',
            'slug',
            'detail',
            'mentor',
            'time',
            'level',
            'course_count',
        ]
