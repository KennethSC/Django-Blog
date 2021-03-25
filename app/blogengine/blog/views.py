from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View


from .models import Post, Tag
from .forms import TagForm, PostForm
from .utils import DetailObjectMixin, CreateObjectMixin

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts': posts})



def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags}) 


class PostDetail(DetailObjectMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(DetailObjectMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
    

class TagCreate(CreateObjectMixin, View):
    model = TagForm
    template = 'blog/tag_create.html' 
        


class PostCreate(CreateObjectMixin, View):
    model = PostForm
    template = 'blog/post_create.html' 
    
