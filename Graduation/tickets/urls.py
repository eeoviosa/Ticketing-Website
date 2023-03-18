from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name = "login"),
    path("", views.index, name = "index"),
    path("add", views.add, name ='add'),
    #path("view", views.view, name = "view")
]