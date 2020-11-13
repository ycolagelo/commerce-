from django.urls import reverse
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Listing, Image
from .forms import NewListForm, ImageForm


def index(request):
    """renders the active list template"""
    active_listings = Listing.objects.filter(state="active").all()

    # for listing in active_listings:
    #     listing.image.image

    return render(request, "auctions/index.html", {
        "active_listings": active_listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_list(request):
    """ creating a new list entry by the user"""
    if request.method == "POST":
        form = NewListForm(request.POST)
        form_a = ImageForm(request.POST, request.FILES)

        if form.is_valid() or form_a.is_valid():

            form.save()
            form_a.save()
            return HttpResponseRedirect(reverse("index"))

        else:
            return render(request, "auctions/create_list.html", {
                "message": "All required information must be provided."
            })
    else:
        form = NewListForm()
        form_a = ImageForm()

        return render(request, "auctions/create_list.html", {
            "form": form, "form_a": form_a
        })
