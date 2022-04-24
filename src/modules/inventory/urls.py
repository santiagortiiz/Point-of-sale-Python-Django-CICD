# Django
from django.urls import include, path

# DRF
from rest_framework.routers import DefaultRouter

# Views
from .views import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls))
]
