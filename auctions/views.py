from django.urls import reverse
from django.db.models import Max, FloatField
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing, Choices, Watchlist, Bid
from .forms import NewListForm, NewBid
from .error_codes import INVALID_BID, ERROR_MESSAGES


def index(request):
    """renders the active list template"""
    active_listings = Listing.objects.filter(state="active").all()

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
        form = NewListForm(request.POST, request.FILES)

        if form.is_valid():
            obj = Listing()

            obj.price = form.cleaned_data['price']
            obj.name = form.cleaned_data['name']
            obj.description = form.cleaned_data['description']
            obj.category = form.cleaned_data['category']
            obj.image = request.FILES['image']
            obj.save()

            return HttpResponseRedirect(reverse("index"))

        return render(request, "auctions/create_list.html", {
            "message": "All required information must be provided."
        })

    return render(request, "auctions/create_list.html", {
        'category_choices': Choices

    })


def listing(request, item_id):
    if request.method == "GET":
        product = Listing.objects.get(pk=item_id)
        lister = product.user_id
        bids = Bid.objects.filter(listing=product).all()
        aggregate_result = bids.aggregate(
            max=Max('bidding_price', output_field=FloatField()))
        highest_bid = aggregate_result['max']
        user = request.user
        # value, category = (product.category)

    return render(request, "auctions/listing.html", {
        "product": product,
        "lister": lister,
        "highest_bid": highest_bid,
        "user": user,
        # "category": category
    })


def watchlist(request, product_id):
    """update the watchlist"""
    listing = Listing.objects.get(pk=product_id)
    user = request.user
    watchlist_products = Watchlist.objects.filter(
        user_id=user.id).all()

    is_in = False
    for w_p in watchlist_products:
        if listing == w_p.listing:
            is_in = True

    if is_in:

        return render(request, "auctions/watchlist.html", {
            "listing": listing
        })

    new_watchlist = Watchlist(user=request.user, listing=listing)
    new_watchlist.save()
    return HttpResponseRedirect(reverse("current_watchlist"))


def current_watchlist(request):
    """Lists all the items in the users watchlist"""
    user = request.user
    listings = Watchlist.objects.filter(user_id=user.id).all()

    return render(request, "auctions/current_watchlist.html", {
        "listings": listings
    })


def watchlist_delete(request, listing_id):
    """delete item that is duplicated in the watchlist"""
    item = get_object_or_404(Watchlist, listing=listing_id)
    if request.method == "POST":
        item.delete()
    return HttpResponseRedirect(reverse("current_watchlist"))


def place_bid(request, product_id):
    """Allows user to place bid on an item"""
    user = request.user
    listing = Listing.objects.get(pk=product_id)
    bids = Bid.objects.filter(listing=listing).all()
    original_price = Listing.objects.get(pk=product_id)

    if request.method == "POST":
        form = NewBid(request.POST)
        obj = Bid()
        if form.is_valid():
            current_bid = form.cleaned_data['bid']
            aggregate_result = bids.aggregate(
                max=Max('bidding_price', output_field=FloatField()))
            max_bidding_price = aggregate_result['max'] or 0

            if current_bid >= original_price.price and current_bid > max_bidding_price:
                obj.listing = listing
                obj.user = user
                obj.bidding_price = current_bid
                obj.save()
                return HttpResponseRedirect(reverse("current_watchlist"))
            else:
                return redirect("error", code=INVALID_BID)
        else:
            return redirect("error", code=INVALID_BID)

    return HttpResponseRedirect(reverse("current_watchlist"))


def error(request, code):
    """generates errors"""
    error_messages = ERROR_MESSAGES[code]
    return render(request, 'auctions/error.html', {
        "error": error_messages
    })
