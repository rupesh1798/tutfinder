from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.contrib.auth import get_user_model
from profile.models import Profile
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    Serializer,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

User = get_user_model()

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate_email(self, value):
        data = self.get_initial()
        email1 = value
        email2 = data.get("email")
        if email1 != email2:
            raise ValidationError("Emails must match")

        user_qs = User.objects.filter(email=email1)
        if user_qs.exists():
            raise ValidationError("This user has already registered")
        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Address', required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or email is required to login")

        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is invalid")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials")
        data["token"] = "some random token"

        return data



# Serializer for password change endpoint.
class ChangePasswordSerializer(Serializer):
    old_password = CharField(required=True)
    new_password = CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class ProfileSerializer(ModelSerializer):
    user = UserDetailSerializer()
    image = SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'user',
            'bio',
            'birth_date',
            'image',
            'fb_url',
            'twitter_url',
            'linkedin_url',
            'website_url',
            'created_at',
        ]
        read_only_fields = ('user','created_at')

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return 'https://static.productionready.io/images/smiley-cyrus.jpg'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        profile = Profile.objects.create(**validated_data)
        User.objects.create(profile=profile, **user_data)
        return profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        username = user_data.pop('username')
        user = get_user_model().objects.get_or_create(username=username)[0]
        user.email = user_data.get(
            'email',
            user.email
        )
        user.first_name = user_data.get(
            'first_name',
            user.first_name
        )
        user.last_name = user_data.get(
            'last_name',
            user.last_name
        )
        user.save()
        instance.user = user
        instance.bio = validated_data.get('bio', instance.bio)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.image = validated_data.get('image', instance.image)
        instance.fb_url = validated_data.get('fb_url', instance.fb_url)
        instance.twitter_url = validated_data.get('twitter_url', instance.twitter_url)
        instance.linkedin_url = validated_data.get('linkedin_url', instance.linkedin_url)
        instance.website_url = validated_data.get('website_url', instance.website_url)

        instance.save()

        return instance
    '''def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        # Unless the application properly enforces that this field is
        # always set, the follow could raise a `DoesNotExist`, which
        # would need to be handled.
        user = instance.user

        #instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        user.username = user_data.get(
            'username',
            user.username
        )
        user.email = user_data.get(
            'email',
            user.email
        )
        user.first_name = user_data.get(
            'first_name',
            user.first_name
        )
        user.last_name = user_data.get(
            'last_name',
            user.last_name
        )
        user.save()

        return instance'''