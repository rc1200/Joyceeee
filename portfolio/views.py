from django.shortcuts import render


def index(request):
    return render(request, "portfolio/index.html")


def index2(request):
    # carousel_img = {'c_imgs': ['assets/img/c1.jpg', 'assets/img/c2.jpg', 'assets/img/c3.jpg'],
    # 'person': [{'nn': 'ron', 'xx':'ronx'}, {'nn': 'aidan', 'xx':'ronyy'}]}
    carousel_stuff = {'stuff': [{'img': 'assets/img/c1.jpg', 'heading': 'heading1', 'is_active': 'active'},
                                {'img': 'assets/img/c2.jpg', 'heading': 'heading2', 'is_active': ''},
                                {'img': 'assets/img/c3.jpg', 'heading': 'heading3', 'is_active': ''}
                                ]}

    return render(request, "portfolio/index2.html", carousel_stuff)

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
