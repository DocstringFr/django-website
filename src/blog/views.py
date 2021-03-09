from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from blog.models import BlogPost


def blog_posts(request):
    posts = BlogPost.objects.all()

    return render(request, "blog/index.html", context={"posts": posts})


def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)

    return render(request, "blog/post.html", context={"post": post})
