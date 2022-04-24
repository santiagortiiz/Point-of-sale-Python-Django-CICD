# DRF
from rest_framework.mixins import DestroyModelMixin


class DeactivateModelMixin(DestroyModelMixin):
    ''' Disable a model instance. '''

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()