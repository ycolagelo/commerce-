from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_list", views.create_list, name="create_list"),
    path("<int:item_id>/details", views.details, name="details"),
    path("<int:product_id>/watchlist", views.watchlist, name="watchlist"),
    path("current_watchlist", views.current_watchlist, name="current_watchlist"),
    path("<int:listing_id>/watchlist_delete",
         views.watchlist_delete, name="watchlist_delete"),
    # path("<int:product_listing_id/delete_list>",
    #  views.delete_list, name="delete_list")
]
