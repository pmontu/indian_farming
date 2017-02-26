from django.db import models


class Order(models.Model):
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