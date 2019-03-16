from django.shortcuts import render, get_object_or_404
from .models import Carousel
from .forms import ContactMeForm

def index(request):
    return render(request, "portfolio/index.html",  {'form': ContactMeForm()})


def index2(request):
    # ensure that the only active record is the one where carousel_num = 1
    Carousel.objects.all().update(is_active=None)
    Carousel.objects.filter(carousel_num=0).update(is_active='active')
    carousel_model = Carousel.objects.all().order_by('carousel_num')
    stuff_for_frontend = {'carousel_model': carousel_model, 'form': ContactMeForm()}
    return render(request, "portfolio/index2.html", stuff_for_frontend)


def index3(request):

    if request.method == 'POST':
        form = ContactMeForm(request.POST)  # if post then capture all that data and store it in an object
        if form.is_valid():  # ensure the form has clean data passed
            print(form.cleaned_data['senderEmail'])
            print(form.cleaned_data['message'])

            # post = form.save(commit=False)
            # post.author = request.user
            # # post.published_date = timezone.now()
            # post.save()
            # # return redirect('post_detail', pk=post.pk)
            # return redirect('post_detail', pk=post.pk)
    else:
        pass

    return render(request, "portfolio/index3.html", {'form': ContactMeForm()})




def contactMeLogic(request):

    if request.method == 'POST':
        form = ContactMeForm(request.POST)  # if post then capture all that data and store it in an object
        if form.is_valid():  # ensure the form has clean data passed
            print(form.cleaned_data['senderEmail'])
            print(form.cleaned_data['message'])
            print('add logic to send email')


def gallery(request):
    contactMeLogic(request)
    return render(request, "portfolio/gallery.html", {'form': ContactMeForm()})



