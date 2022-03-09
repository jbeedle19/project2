from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_comment", views.comment, name="comment"),
    path("add_watch", views.add_watch, name="add"),
    path("bid", views.bid, name="bid"),
    path("categories", views.categories, name="categories"),
    path("categories/<int:id>/<str:category>", views.category, name="category"),
    path("close", views.close, name="close"),
    path("create", views.create, name="create"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("remove_watch", views.remove_watch, name="remove"),
    path("watchlist", views.watchlist, name="watchlist")
]