from django.db import models


class ContactUs(models.Model):
    company_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=12)
    role = models.CharField(max_length=200)
    aggriculture_produce = models.CharField(max_length=200)
    variety = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    quality_specification = models.CharField(max_length=200)
    delivery_place = models.CharField(max_length=200)
    expected_date_of_delivery = models.DateField()
