

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date
from .models import Post





def index(request):
    posts = Post.objects.all().order_by("-date")[:4]
    return render(request, "blog/index.html", {
        "new_posts": posts
    })

def projects(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/list.html", {
        "posts": posts
    })
def single_blog(request, slug):
    single_post = get_object_or_404(Post, slug=slug)
            
    return render(request, "blog/single_blog.html", {
        "single_posts": single_post
    })