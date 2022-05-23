def default_user_authentication_rule(user):
    '''
    Function to be used by the simple-jwt library and it's specified in the SIMPLE_JWT settings.

    Callable to determine if the user is permitted to authenticate.
    This rule is applied after a valid token is processed.
    The user object is passed to the callable as an argument.
    The default rule is to check that the is_active flag is still True.
    The callable must return a boolean, True if authorized, False otherwise resulting in a 401 status code.

    Ref: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html#user-authentication-rule
    '''
    return user is not None and user.is_active