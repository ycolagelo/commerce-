from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_list", views.create_list, name="create_list"),
    path("<int:item_id>/listing", views.listing, name="listing"),
    path("<int:product_id>/watchlist", views.watchlist, name="watchlist"),
    path("current_watchlist", views.current_watchlist, name="current_watchlist"),
    path("<int:listing_id>/watchlist_delete",
         views.watchlist_delete, name="watchlist_delete"),
    path("<int:product_id>/place_bid", views.place_bid, name="place_bid"),
    path("error/<int:code>", views.error, name="error"),
    path("<int:product_id>/comment", views.comment, name="comment"),
    path("<str:choice>/category", views.category, name="category")
]
