# Django
from django.db import models

# Utilities
from modules.utils.models import BaseModel


class OrderItem(BaseModel):

    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.PROTECT
    )

    product = models.ForeignKey(
        'inventory.Product',
        on_delete=models.PROTECT
    )

    description = models.CharField(
        max_length=255,
        help_text='Description of the product at the time of purchase'
    )

    quantity = models.PositiveIntegerField(
        default=1,
        help_text='Requested units'
    )

    unit_price = models.PositiveIntegerField(
        'unit price',
        default=0,
        help_text='unit price in cents'
    )

    total = models.PositiveIntegerField(
        default=0,
        help_text='formula: total = unit_price x quantity'
    )


    class Meta:
        db_table = 'order_items'


class Order(BaseModel):

    products = models.ManyToManyField(
        'inventory.Product',
        through='OrderItem',
        through_fields=('order', 'product'),
    )

    total = models.PositiveIntegerField(
        default=0,
        help_text='Price in cents'
    )


    class Meta:
        db_table = 'orders'
        get_latest_by = 'created'
        ordering = ['-created', '-modified']