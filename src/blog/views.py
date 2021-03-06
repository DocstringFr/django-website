from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from blog.models import BlogPost


@user_passes_test(lambda u: "Modérateurs" in [group.name for group in u.groups.all()])
def blog_posts(request):
    blog_post = get_object_or_404(BlogPost, pk=3)

    return HttpResponse(blog_post.content)
