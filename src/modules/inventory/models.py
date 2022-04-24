# Django
from django.db import models

# Utilities
from modules.utils.models import BaseModel


class Product(BaseModel):

    description = models.CharField(
        max_length=255,
        help_text='brief product description, (up to 255 characters)'
    )

    unit_price =  models.PositiveIntegerField(
        'unit price',
        default=0,
        help_text='unit price in cents'
    )

    stock = models.PositiveSmallIntegerField(
        default=0,
        help_text='Available units'
    )


    class Meta:
        db_table = 'products'
        get_latest_by = 'created'
        ordering = ['-created', '-modified']


    def __str__(self):
        return f'{self.description}'