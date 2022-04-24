# Django
from django.db import transaction

# DRF
from rest_framework import mixins, viewsets

# Permissions
from rest_framework.permissions import AllowAny

# Models
from modules.orders.models import Order

# Serializers
from modules.orders.serializers import OrderModelSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    ''' Viewset for orders management. '''

    queryset = Order.objects.filter(active=True)
    permission_classes = [AllowAny]
    serializer_class = OrderModelSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)