from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from app_user.models import User


class DeliveryPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=9)
    salary = models.FloatField(
        validators=[MinValueValidator(0.01)],
    )
#   where they work, will reference restaurants table
    restaurant = models.ForeignKey(
        'restaurant.Restaurant',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
    )
    # rating (0 - 5) will reference Rating table/app
    # TODO: Ratings object related to person at restaurant
    # rating = models.ManyToManyField(
    #     'ratings.Rating', through='restaurant.Restaurant')
#   if cook gets warned more than 3 times they get a warning
    warnings = models.PositiveIntegerField(
        validators=[MaxValueValidator(3)],
        default=0,
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Delivery(models.Model):
    STATUSES = [
        (1, 'New'),
        (2, 'Open To Bid'),
        (3, 'Active'),
        (4, 'Completed')
    ]
    status = models.PositiveIntegerField(choices = STATUSES, default = 1)

    who_delivered = models.ForeignKey(
        DeliveryPerson,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    to_customer = models.ForeignKey(
        'customer.Customer',
        on_delete=models.SET_NULL,
        null=True,
         blank=True,
    )

    rating = models.ForeignKey(
        'ratings.rating',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    notes = models.CharField(
        max_length=100,
        blank=True,
        default='',
    )
