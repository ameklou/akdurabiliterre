from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.index, name="presta"),
    #url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.index, name='post_list_by_tag'),
    url(r'^(?P<slug>[\w-]+)-(?P<category>[\w-]+)-(?P<city>[\w]+)/$',
        views.presta_detail,
        name='presta_detail'),


]
