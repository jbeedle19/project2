from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_comment", views.comment, name="comment"),
    path("create", views.create, name="create"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]