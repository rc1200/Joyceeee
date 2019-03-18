from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path("", views.index, name="index"),
    path("index2", views.index2, name="index2"),
    path("index3", views.index3, name="index3"),
    path("gallery", views.gallery, name="gallery"),
    path("thankyou", views.thankyou, name="thankyou"),

]
