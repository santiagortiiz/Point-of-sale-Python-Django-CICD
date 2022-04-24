# Django
from django.db import models


class BaseModel(models.Model):
    """
    BaseModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
        + active (Boolean): Store the flag that indicates if the record was deleted or not.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )
    active = models.BooleanField(
        'active or not',
        default=True,
        help_text='''
            Designates whether this user should be treated as active.
            Unselect this instead of deleting accounts.
        '''
    )


    class Meta:

        abstract = True
