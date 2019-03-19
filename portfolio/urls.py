from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
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

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

