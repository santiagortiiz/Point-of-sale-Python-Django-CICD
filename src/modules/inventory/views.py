# DRF
from rest_framework import mixins, viewsets, filters

# Permissions
from rest_framework.permissions import AllowAny

# Models
from modules.inventory.models import Product

# Serializers
from modules.inventory.serializers import ProductModelSerializer


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    '''
    Viewset for products management.
    Allows:
        - "CRU" operations.
        - Search a product by a text contained in the description.
    '''

    permission_classes = [AllowAny]
    queryset = Product.objects.filter(active=True)
    serializer_class = ProductModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']