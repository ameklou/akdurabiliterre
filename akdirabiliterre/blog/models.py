from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.


class Category(models.Model):
    """
        Blog aricle category
    """
    name = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
       def get_queryset(self):
           return super(PublishedManager,
                        self).get_queryset()\
                             .filter(status='published')


class Post(models.Model):
    """
        Blog Posts
    """

    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),
    )
    title = models.CharField(max_length=250)
    cover=models.ImageField(upload_to="cover")
    body= models.TextField()
    category = models.ForeignKey(Category, related_name='post_category', on_delete=models.CASCADE)
    slug= models.SlugField(max_length=250, unique_for_date="publish")
    author=models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
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
        return reverse('post_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
