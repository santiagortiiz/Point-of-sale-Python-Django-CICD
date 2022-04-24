# DRF
from rest_framework import serializers

# Models
from modules.inventory.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    ''' Model Serializer for products. '''

    class Meta:
        model = Product
        exclude = ['created', 'modified', 'active']