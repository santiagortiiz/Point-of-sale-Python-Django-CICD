# Django
from django.forms.models import model_to_dict

# DRF
from rest_framework import serializers

# Models
from modules.inventory.models import Product
from modules.orders.models import Order, OrderItem


class OrderItemSerializer(serializers.Serializer):
    '''
    Defines the structure of the data required to generate an order with
    the requested items and validates their availability.

    Data structure:
        {
            "id": <product_id>,
            "quantity": <positive integer>
        }
    '''

    id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(active=True)
    )
    quantity = serializers.IntegerField(min_value=1)

    def to_internal_value(self, data):
        ''' Rename the input data for the OrderModelSerializer '''
        order_item = super().to_internal_value(data)

        # Replace 'id' name field by 'product'
        order_item['product'] = order_item.pop('id')
        # Add the current description of the product
        order_item['description'] = order_item['product'].description
        # Adds to the order the current unit price of the product
        order_item['unit_price'] = order_item['product'].unit_price
        return order_item

    def validate(self, attrs):
        ''' Validates the stock is sufficient to meet the quantity requested '''
        product = attrs['product']
        quantity = attrs['quantity']

        if quantity < 1:
            raise serializers.ValidationError(f'quantity must be greather than zero')

        if product.stock < quantity:
            raise serializers.ValidationError(f'Insufficient stock for {product.description} ')

        return attrs


class OrderModelSerializer(serializers.ModelSerializer):
    '''
    Model Serializer for the orders.
    Manage creation and reading of an order with its items.
    '''

    items = OrderItemSerializer(
        many=True,
        write_only=True
    )


    class Meta:
        model = Order
        fields = ['id', 'items', 'total']
        read_only_fields = ['total']


    def create(self, validated_data):
        ''' Creates an order with the requested items and updates the stock '''
        # Creates an order
        items = validated_data.pop('items')
        order = super().create(validated_data)

        order_items = []
        updated_products = []

        for item in items:
            # Creates the items of the order
            total_item_price = item['unit_price'] * item['quantity']
            order_items.append(
                OrderItem(order=order, **item, total=total_item_price)
            )

            # Updates the stock for the requested product
            product = item['product']
            product.stock -= item['quantity']
            updated_products.append(product)

            # Updates the total price for the order
            order.total += total_item_price

        Product.objects.bulk_update(updated_products, ['stock'])
        OrderItem.objects.bulk_create(order_items)

        order.save()
        return order

    def to_representation(self, instance):
        ''' Adds the items of an order in a readable format '''
        order = super().to_representation(instance)
        order['items'] =  [
            model_to_dict(
                item,
                fields=['description', 'quantity', 'unit_price', 'total']
            )
            for item in instance.orderitem_set.all()
        ]
        return order