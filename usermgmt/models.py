from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    FARMER = 'FR'
    CUSTOMER = 'CS'
    SPECIAL_USER_CHOICES = (
        (FARMER, 'Farmer'),
        (CUSTOMER, 'Customer'),
    )
    user_type = models.CharField(
        max_length=2,
        choices=SPECIAL_USER_CHOICES,
        default=CUSTOMER,
    )
