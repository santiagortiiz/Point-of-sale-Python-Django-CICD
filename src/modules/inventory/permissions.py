from rest_access_policy import AccessPolicy


class InventoryPolicy(AccessPolicy):

    statements = [
        {
            'action': '*',
            'principal': ['group:seller'],
            'effect': 'allow'
        },
        {
            'action': ['list', 'retrieve'],
            'principal': '*',
            'effect': 'allow'
        }
    ]