from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse

from django.views.generic import DetailView, TemplateView, ListView, CreateView, UpdateView, DeleteView

from blog.forms import BlogPostForm
from blog.models import BlogPost


class BlogIndexView(ListView):
    model = BlogPost
    template_name = "blog/index.html"
    context_object_name = "posts"


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post.html"
    context_object_name = "post"


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "blog/create_post.html"
    form_class = BlogPostForm

    def get_success_url(self):
        return reverse("blog-index")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user

        form.instance.published = True

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Créer"
        return context


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog/create_post.html"
    form_class = BlogPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Modifier"
        return context


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/delete_post.html"
    context_object_name = "post"
    success_url = reverse_lazy("blog-index")


def blog_posts(request):
    posts = BlogPost.objects.filter(published=True)

    return render(request, "blog/index.html", context={"posts": posts})


def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)

    return render(request, "blog/post.html", context={"post": post})


def blog_post_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.instance.published = True
            if request.user.is_authenticated:
                form.instance.author = request.user
            form.save()
            return HttpResponseRedirect(reverse("blog-index"))
    else:
        form = BlogPostForm()

    return render(request, "blog/create_post.html", {"form": form})
