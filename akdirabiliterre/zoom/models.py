from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
# Create your models here.


class PublishedManager(models.Manager):
       def get_queryset(self):
           return super(PublishedManager,
                        self).get_queryset()\
                             .filter(status='published')


class Zoom(models.Model):


    STATUS_CHOICES=(
    ('draft','draft'),
    ('published','published'),
    )
    title=models.CharField(max_length=250)
    architect = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    engineer= models.CharField(max_length=250, null= True, blank=True)
    designer= models.CharField(max_length=250, null= True, blank=True)
    project_year= models.DateField(default=timezone.now)
    site_area = models.CharField(max_length=250, null=True, blank=True)
    cover=models.ImageField(upload_to='zoom_cover')
    pictures=models.FileField(upload_to='zoom_pictures')
    content_fr = models.TextField()
    content_en=models.TextField()
    slug= models.SlugField(max_length=250, unique_for_date="publish")
    author=models.ForeignKey(User, related_name="zoom_zooms")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    main= models.BooleanField(default=False)
    status = models.CharField(max_length=10,
                                 choices=STATUS_CHOICES,
                                 default='draft')
    tags = TaggableManager()

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
           ordering = ('-publish',)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('zoom_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])
