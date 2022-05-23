# Django
from django.conf import settings

# DRF
from rest_framework import serializers

# Models
from django.contrib.auth.models import Group
from modules.users.models import User


class UserModelSerializer(serializers.ModelSerializer):

    password_confirmation = serializers.CharField(min_length=4, max_length=64, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def validate(self, attrs):
        '''
        Validate that the password entered and its confirmation are the same.
        '''
        view = self.context['view']
        if view.action == 'create':

            password = attrs['password']
            password_confirmation = attrs.pop('password_confirmation')

            if password != password_confirmation:
                raise serializers.ValidationError("Passwords do not match")

        else:
            if 'password' in attrs:
                # Remove the password if there is an attempt to change it
                attrs.pop('password')

        return super().validate(attrs)

    def create(self, validated_data):
        '''
        Adds the user that will be created to the default group
        '''
        user = User.objects.create_user(**validated_data)
        default_group = Group.objects.get(name=settings.DEFAULT_USER_GROUP)
        user.groups.set([default_group])
        return user