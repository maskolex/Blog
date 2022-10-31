from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from blog import settings
from deflor.views import *

urlpatterns = [
    path('', index, name="home_page"),
    path('about/', about, name="about"),
    path('feedback/', feedback, name="feedback"),
    path('add_page/', add_page, name="add_page"),
    path('login/', login, name="login"),
    path('post/<slug:post_slug>', show_actor, name="show"),
    path('category/<slug:cat_slug>', show_category, name="category"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

