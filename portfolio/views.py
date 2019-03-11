from django.shortcuts import render


def index(request):
    return render(request, "portfolio/index.html")


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
