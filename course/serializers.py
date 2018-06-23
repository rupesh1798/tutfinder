from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from .models import Course, SubmitCourse
#from review.models import Review
# from django.contrib.auth.models import User


course_detail_url = HyperlinkedIdentityField(
    view_name = 'course:course_detail', #related name in urls
    lookup_field = 'slug'
)

class CourseCreateUpdateSerializer(ModelSerializer):
    # tech = SerializerMethodField()
    submitter = SerializerMethodField()
    #tutor = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'tech',
            'submitter',
            'tutor',
            'title',
            'detail',
            'image',
            'logo',
            'logo_url',
            'free',
            'level',
            'medium',
        ]
    #def get_tech(self, obj):
    #    return str(obj.tech.title)
    def get_submitter(self, obj):
        return str(obj.submitter.username)
    #def get_tutor(self, obj):
    #    return str(obj.tutor.username)
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image

class CourseListSerializer(ModelSerializer):
    url = course_detail_url
    tech = SerializerMethodField()
    submitter = SerializerMethodField()
    tutor = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'id',
            'tech',
            'submitter',
            'tutor',
            'title',
            'slug',
            'url',
            'detail',
            'image',
            'logo',
            'logo_url',
            'upvotes',
            'free',
            'level',
            'medium',
        ]
    def get_tech(self, obj):
        return str(obj.tech.title)
    def get_submitter(self, obj):
        return str(obj.submitter.username)
    def get_tutor(self, obj):
        return str(obj.tutor.username)
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image

class CourseDetailSerializer(ModelSerializer):
    tech = SerializerMethodField()
    submitter = SerializerMethodField()
    tutor = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'id',
            'tech',
            'submitter',
            'tutor',
            'title',
            'slug',
            'url',
            'detail',
            'image',
            'logo',
            'logo_url',
            'upvotes',
            'free',
            'level',
            'medium',
        ]
    def get_tech(self, obj):
        return str(obj.tech.title)
    def get_submitter(self, obj):
        return str(obj.submitter.username)
    def get_tutor(self, obj):
        return str(obj.tutor.username)
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image

class CourseDeleteSerializer(ModelSerializer):
    tech = SerializerMethodField()
    submitter = SerializerMethodField()
    tutor = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Course
        fields = [
            'tech',
            'submitter',
            'tutor',
            'title',
            'detail',
            'image',
            'logo',
            'logo_url',
            'free',
            'level',
            'medium',
        ]
    def get_tech(self, obj):
        return str(obj.tech.title)
    def get_submitter(self, obj):
        return str(obj.submitter.username)
    def get_tutor(self, obj):
        return str(obj.tutor.username)
    def get_image(self, obj):
        try:
            image = obj.logo.url
        except:
            image = None
        return image


class SubmitCourseCreateUpdateSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = SubmitCourse
        fields = [
            'user',
            'url',
            'detail',
            'free',
            'level',
            'medium',
        ]
    def get_user(self, obj):
        return str(obj.user.username)
    #def get_tutor(self, obj):
    #    return str(obj.tutor.username)
