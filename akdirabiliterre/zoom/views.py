from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
#from django.core.mail import send_mail
from django.db.models import Count
from .models import Zoom
from blog.models import Post
from taggit.models import Tag
from blog.models import Post
#from .forms import EmailPostForm, CommentForm

# Create your views here.


def index(request, tag_slug=None):
    object_list = Zoom.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    zooms = object_list
    lasts= Post.published.all()[:3]

    #paginator = Paginator(object_list, 3) # 3 posts in each page
    #page = request.GET.get('page')
    #try:
    #    posts = paginator.page(page)
    #except PageNotAnInteger:
        # If page is not an integer deliver the first page
        #posts = paginator.page(1)
    #except EmptyPage:
        # If page is out of range deliver last page of results
        #posts = paginator.page(paginator.num_pages)
    return render(request, 'zoom/index.html', {'zooms': zooms,
                                                'lasts':lasts,
                                                   'tag': tag})


def zoom_detail(request, year, month, day, post):
    post = get_object_or_404(Zoom, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)






    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    posts=Post.published.all()[:3]
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags',
                                                                             '-publish')[:4]
    return render(request, 'zoom/detail.html', {'post': post,
                                                     'similar_posts': similar_posts,
                                                     'posts':posts
                                                     })
