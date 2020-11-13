from django.contrib import admin

# Register your models here.
from .models import Listing, Bid, Comment


class ListingsAdmin(admin.ModelAdmin):
    list_display = ("id", "price", "description", "state", "category", "image")


admin.site.register(Listing, ListingsAdmin)
admin.site.register(Bid)
admin.site.register(Comment)
