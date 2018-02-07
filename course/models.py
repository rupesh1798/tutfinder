from django.db import models
from django.contrib.auth.models import Permission, User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class Course(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
#    langauge =
    title = models.CharField(max_length=255, blank=True, null=True)
    free = models.BooleanField(default=True, blank=False)
#    active
#    price
#    type choice = book, video, course
    LEVEL = (('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'),
               ('ADVANCED', 'Advanced'))
    level = models.CharField(choices=LEVEL, default='Select', max_length=20, blank=False)
#    advanced begineeer, inter
#    expexted duration
    upvotes= models.IntegerField(blank=True, null=True)
#    tech =
