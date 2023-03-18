from django.urls import path
from . import views

urlpatterns = [
    path("login", views.logn, name = "login"),
    path("", views.index, name = "index"),
    path("add", views.add, name ='add'),
    path("logout", views.logt name = 'logout')
    #path("view", views.view, name = "view")
]