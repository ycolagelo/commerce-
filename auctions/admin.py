from django.contrib import admin

# Register your models here.
from .models import Listing, Bid, Comment, Watchlist


class ListingsAdmin(admin.ModelAdmin):
    list_display = ("id", "price", "description", "state",
                    "category", "image", "user_id")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "listing", "comments")


admin.site.register(Listing, ListingsAdmin)
admin.site.register(Bid)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Watchlist)
