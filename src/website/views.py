from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


def home(request):
    return render(request, "index.html", {"title": "Accueil du site"})
