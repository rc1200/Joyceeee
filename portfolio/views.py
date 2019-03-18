from django.shortcuts import render, get_object_or_404
from .models import Carousel
from .forms import ContactMeForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect

def thankyou(request):
    form = ContactMeForm(request.POST or None)

    if form.is_valid():  # ensure the form has clean data passed

        messages.success(request, 'thank you we will contact you')

        save_it = form.save(commit=False)
        # save_it.save()
        # send email
        subject = 'Message from Client'
        message = form.cleaned_data['message']
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_it.senderEmail, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fail_silently=False,)

        messages.success(request, 'thank you we will contact you')
        return HttpResponseRedirect('/', {'form': ContactMeForm()})


def index(request):
    messages.success(request, 'thank you we will contact you')
    return render(request, "portfolio/index.html", {'form': ContactMeForm()})


def index2(request):
    # ensure that the only active record is the one where carousel_num = 1
    Carousel.objects.all().update(is_active=None)
    Carousel.objects.filter(carousel_num=0).update(is_active='active')
    carousel_model = Carousel.objects.all().order_by('carousel_num')
    stuff_for_frontend = {'carousel_model': carousel_model, 'form': ContactMeForm()}
    return render(request, "portfolio/index2.html", stuff_for_frontend)
    # return render(request, "portfolio/index2.html",  {'form': ContactMeForm()})


def index3(request):
    if request.method == 'POST':
        form = ContactMeForm(request.POST)  # if post then capture all that data and store it in an object
        if form.is_valid():  # ensure the form has clean data passed
            print(form.cleaned_data['senderEmail'])
            print(form.cleaned_data['message'])

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
