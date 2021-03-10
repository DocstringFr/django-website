from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from website.forms import SignupForm, BlogPostForm


def home(request):
    return HttpResponse("Accueil du site !")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Merci de vous être inscrit au site.")
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})


def blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        init_values = {}
        if request.user.is_authenticated:
            init_values["author"] = request.user
        init_values["date"] = datetime.today()
        form = BlogPostForm(initial=init_values)

    return render(request, "blog/post.html", {"form": form})
