from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import Permission, User
from technology.models import Technology


class Track(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    # tech = models.ForeignKey(Technology, default=None, on_delete=models.CASCADE)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='mentor')
    slug = models.SlugField(unique=True, blank=True)
    detail = models.TextField(blank=True)
    time = models.IntegerField(default=0, blank=False) #min
    course_count = models.IntegerField(default=0, blank=True)
    LEVEL = (('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'),
             ('ADVANCED', 'Advanced'))
    level = models.CharField(choices=LEVEL, default='Select', max_length=20, blank=False)
    featured = models.BooleanField(default=False, blank=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Technology, self).save(*args, **kwargs)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Track.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_technology_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_technology_receiver, sender=Track)
