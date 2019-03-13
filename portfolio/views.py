from django.shortcuts import render, get_object_or_404
from .models import Carousel


def index(request):
    return render(request, "portfolio/index.html")


def index2(request):
    carousel_model = Carousel.objects.all().order_by('carousel_num')
    stuff_for_frontend = {'carousel_model': carousel_model}
    return render(request, "portfolio/index2.html", stuff_for_frontend)

# include templates


def header(request):
    return render(request, "portfolio/header.html")


def myCarousel(request):
    return render(request, "portfolio/myCarousel.html")


def marketing(request):
    return render(request, "portfolio/marketing.html")


def myCarousel(request):
    return render(request, "portfolio/myCarousel.html")


def featurettes(request):
    return render(request, "portfolio/featurettes.html")


def footer(request):
    return render(request, "portfolio/footer.html")
