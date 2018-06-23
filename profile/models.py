from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_pic(instance, filename):
    return '/'.join(['Images/Profile', instance.user.username])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    first_name = models.CharField(max_length=50, blank=True)
#    last_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True)
#    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to=profile_pic, blank=True,)
    fb_url = models.URLField(default='', blank=True)
    twitter_url = models.URLField(default='', blank=True)
    linkedin_url = models.URLField(default='', blank=True)
    website_url = models.URLField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()