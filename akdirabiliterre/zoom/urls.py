from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.index, name="zoom"),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.index, name='post_list_by_tag'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.zoom_detail,
        name='zoom_detail'),


]
