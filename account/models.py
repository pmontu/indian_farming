from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """
    Records Customer Orders and Farmers Produce
    """
    CROP_CHOICES = (
        ("RI", "Rice"),
        ("WH", "Wheat"),
        ("PL", "Pulses"),
        ("MZ", "Maize"),
        ("ML", "Millets")
    )
    crop = models.CharField(max_length=2, choices=CROP_CHOICES)
    CITY_CHOICES = (
        ("CH", "Chennai"),
        ("MB", "Mumbai"),
        ("KT", "Kokkatta"),
        ("DH", "Delhi"),
        ("HD", "Hyderbad"),
        ("BL", "Banglore")
    )
    city = models.CharField(max_length=2, choices=CITY_CHOICES)
    volume = models.PositiveIntegerField()
    delivery_date = models.DateField()
    entry_by = models.ForeignKey(User)
    ORDER = "O"
    PRODUCE = "P"
    ENTRY_TYPES = (
        (ORDER, "Order"),
        (PRODUCE, "Produce")
    )
    entry = models.CharField(choices=ENTRY_TYPES, max_length=1)
