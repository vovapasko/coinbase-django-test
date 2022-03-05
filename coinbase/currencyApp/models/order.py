import uuid

from django.db import models


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price_amount = models.FloatField()
    price_currency = models.FloatField()
    receive_currency = models.FloatField()
    receive_amount = models.FloatField()
