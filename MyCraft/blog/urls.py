#coding: utf-8
from django.conf.urls import patterns, url
from blog.models import Post

from blog.views import PostsListView, PostDetailView

urlpatterns = patterns('blog.views',
url(r'^$', PostsListView.as_view(queryset=Post.objects.all().order_by('-datetime')), name='list'),
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
url(r'^tag/(?P<id>\w+)/$', 'tag')

)
