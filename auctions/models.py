from django.contrib.auth.models import AbstractUser

from django.db import models
from django.forms import ModelForm


class User(AbstractUser):
    pass


class Choices(models.TextChoices):
    Antique = 'a'
    Electronic = 'b'
    Home = 'c'
    Toys = 'd'
    Education = 'e'
    Clothes = 'f'
    Workout = 'g'
    Fashion = 'h'
    Food = 'i'
    Luxury = 'j'


class Listing(models.Model):
    """Modles for auctions listings"""
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/', null=True)
    user_id = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, related_name="client"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=100)
    state = models.CharField(max_length=30, default="active")
    category = models.CharField(
        max_length=50, choices=Choices.choices)

    def __str__(self):
        return f"{self.description} '$'{self.price} {self.state} {self.category} {self.image}"


class Bid(models.Model):
    """models for the bids created on the listings"""
    product = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="bid_product")
    user_id = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="bidder")
    bidding_price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user_id} placed {self.bidding_price} on {self.product}"


class Comment(models.Model):
    """models for the comments created by the user"""
    item = models.ForeignKey(Listing, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    comments = models.CharField(max_length=280)

    def __str__(self):
        return f"{self.user_id} mentioned {self.comments} on {self.item}"
