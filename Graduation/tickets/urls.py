from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name = "login"),
    path("add", views.add, name = "add"),
    path("view", views.view, name = "view"),
]