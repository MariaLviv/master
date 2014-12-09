from blog.models import Post, Tag
from django.views.generic import ListView, DetailView
from django.shortcuts import render

class PostsListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

def tag (request, id):
    tag = Tag.objects.select_related().get(id=id)
    posts = tag.post_set.all()
    return render(request, 'blog/tagpage.html', {'posts': posts, 'tag': tag})
