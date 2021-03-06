from django.http import HttpResponse


def home(request):
    return HttpResponse("Accueil du site !")
