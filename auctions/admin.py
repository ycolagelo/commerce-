from django.contrib import admin

# Register your models here.
from .models import Listing, Bid, Comment, Image


class ListingsAdmin(admin.ModelAdmin):
    list_display = ("id", "price", "description", "state", "category")


admin.site.register(Listing, ListingsAdmin)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Image)
