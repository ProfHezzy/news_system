from django.urls import path
from . import views
from django.http import HttpResponseNotFound

def catch_all(request, path=None):
    return HttpResponseNotFound("This endpoint does not exist.")

urlpatterns = [
    path('', views.index, name = "index")
]
