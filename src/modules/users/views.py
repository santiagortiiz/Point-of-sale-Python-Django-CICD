# Django
from django.contrib.auth.models import update_last_login

# DRF
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins, viewsets, status

# Models
from .models import User

# Serializers
from .serializers import UserModelSerializer

# Permissions
from .permissions import UserAccessPolicy


class UserViewSet(viewsets.ModelViewSet):

    ''' Viewset for the user's Signup, and general CRUD '''

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    permission_classes = (UserAccessPolicy,)