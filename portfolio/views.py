from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import  FormView
from .models import Carousel
from .forms import ContactMeForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect



# use content mixin instead since we are expanding the base and just need to call the template vs having to explictly
# call the dictionary
class GetContentMixin(object):
    mixin_model = Carousel

    def get_context_data(self, **kwargs):
        Carousel.objects.all().update(is_active=None)
        Carousel.objects.filter(carousel_num=0).update(is_active='active')
        context = super(GetContentMixin, self).get_context_data(**kwargs)
        context['carousel_model'] = self.mixin_model.objects.all().order_by('carousel_num')
        return context


# since the template extends the base which requires a form, we need to create a mixin to define the form
# so the form data can be passed since we hid them and only display them when they try contact them because it is a modal form
class FormMixin(forms.Form):
    form_class = ContactMeForm


# class instead to speed up production
# NOTE: using the mixin for the form and content
class Index3(GetContentMixin, FormMixin, FormView):
    template_name = "portfolio/index2.html" # define the template to use


class gallery3(GetContentMixin, FormMixin, FormView):
    template_name = "portfolio/gallery.html" # define the template to use


# Function Based views

def thankyou(request):
    form = ContactMeForm(request.POST or None)

    if form.is_valid():  # ensure the form has clean data passed
        save_it = form.save(commit=False)

        # save_it.save() # since we are not storing this in the DB no need to save

        # send email
        subject = 'Message from Client'
        message = form.cleaned_data['message']
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_it.senderEmail, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fail_silently=False,)

        return HttpResponseRedirect('/', {'form': ContactMeForm()})


def index(request):
    return render(request, "portfolio/index.html", {'form': ContactMeForm()})


def index2(request):
    # ensure that the only active record is the one where carousel_num = 1
    Carousel.objects.all().update(is_active=None)
    Carousel.objects.filter(carousel_num=0).update(is_active='active')
    carousel_model = Carousel.objects.all().order_by('carousel_num')
    stuff_for_frontend = {'carousel_model': carousel_model, 'form': ContactMeForm()}
    return render(request, "portfolio/index2.html", stuff_for_frontend)
    # return render(request, "portfolio/index2.html",  {'form': ContactMeForm()})


def gallery(request):
    return render(request, "portfolio/gallery.html", {'form': ContactMeForm()})
