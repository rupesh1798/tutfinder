from django.db import models
from django.core.urlresolvers import reverse
from technology.models import Technology
from django.db.models.signals import pre_save
from django.contrib.auth.models import Permission, User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField #does not contain upload option for us in Images
from ckeditor_uploader.fields import  RichTextUploadingField #for adding upload from our own server in CKEDITOR

def course_logo(instance, filename):
    return '/'.join(['Images/course', instance.title])


class SubmitCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='raw_submitter')
    url = models.URLField(default='', blank=True)
    detail = models.TextField(default='', blank=True, null=True)
    free = models.BooleanField(default=True, blank=False)
    LEVEL = (('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'),
             ('ADVANCED', 'Advanced'))
    level = models.CharField(choices=LEVEL, default='Select', max_length=20, blank=False)
    MEDIUM = (('VIDEO', 'Video'), ('TEXT', 'Text'))
    medium = models.CharField(choices=MEDIUM, default='Select', max_length=20, blank=False)


class Course(models.Model):
    tech = models.ForeignKey(Technology, default=None, on_delete=models.CASCADE)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='submitter')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='course_tutor')
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    url = models.URLField(default='', blank=True)
    detail = RichTextUploadingField()
    logo = models.ImageField(upload_to=course_logo, blank=True)
    logo_url = models.URLField(default='', blank=True)
    upvotes = models.ManyToManyField(User, blank=True, related_name='course_upvotes')
    free = models.BooleanField(default=True, blank=False)
    LEVEL = (('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'),
             ('ADVANCED', 'Advanced'))
    level = models.CharField(choices=LEVEL, default='Select', max_length=20, blank=False)
    MEDIUM = (('VIDEO', 'Video'), ('TEXT', 'Text'))
    medium = models.CharField(choices=MEDIUM, default='Select', max_length=20, blank=False)
    featured = models.BooleanField(default=False, blank=False)
    # self paced = bool
    # langauge =
    # active = bool
    # price = int
    # type choice = book, video, course
    # advanced begineeer, inter
    # expexted duration
    # def get_absolute_url(self):
    # certificate
    def __unicode__(self):
        return self.title

    def __str__(self):
        return (self.title + str(self.tech))

    def get_absolute_url(self):
        return reverse("course:course_detail", kwargs={"slug": self.slug})
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Course, self).save(*args, **kwargs)

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Course.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Course)