# Django
from django.urls import include, path

# DRF
from rest_framework.routers import DefaultRouter

# Views
from .views import OrderViewSet

router = DefaultRouter()

router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls))
]
