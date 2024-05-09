from django.urls import path

from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", views.index, name="index"),
    path("two/", csrf_exempt(views.processFile), name="processFile"),

]