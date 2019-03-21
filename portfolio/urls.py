from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.static import serve
from django.conf.urls import url
from . import views
from portfolio.views import Index3, gallery3

app_name = 'portfolio'
urlpatterns = [
    path("", views.index2, name="index"),
    path("index2", views.index2, name="index2", ),
    path("index3", Index3.as_view(), name="index3"),
    path("gallery", views.gallery, name="gallery"),
    path("gallery3", gallery3.as_view(), name="gallery3"),
    path("thankyou", views.thankyou, name="thankyou"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
