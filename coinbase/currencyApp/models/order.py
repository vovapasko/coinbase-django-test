import uuid

from django.db import models


class Order(models.Model):
    max_len_currency_constant = 10

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price_amount = models.FloatField()
    price_currency = models.CharField(max_length=max_len_currency_constant)
    receive_currency = models.CharField(max_length=max_len_currency_constant)
    receive_amount = models.FloatField()
