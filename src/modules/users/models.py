'''Doc: https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#extending-the-existing-user-model'''
'''Groups: https://docs.djangoproject.com/en/3.2/topics/auth/default/#groups'''

# Django
from django.db import models

# Models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField('email address', blank=True, unique=True)