from .order import Order
from django.db import models


class CoingateOrder(Order):
    coingate_order_id = models.PositiveIntegerField(blank=True, null=True)
    receive_amount = models.FloatField(blank=True, null=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    callback_url = models.URLField(null=True, blank=True)
    cancel_url = models.URLField(null=True, blank=True)
    success_url = models.URLField(null=True, blank=True)
    token = models.CharField(max_length=200, null=True, blank=True)
    purchaser_email = models.EmailField(null=True, blank=True)
