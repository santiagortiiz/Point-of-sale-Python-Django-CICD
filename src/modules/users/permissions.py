from rest_access_policy import AccessPolicy


class UserAccessPolicy(AccessPolicy):

    statements = [
        {
            'action': ['create'],
            'principal': '*',
            'effect': 'allow'
        },
        {
            'action': ['list', 'retrieve'],
            'principal': ['group:developer'],
            'effect': 'allow'
        },
        {
            'action': ['retrieve', 'update', 'partial_update', 'delete'],
            'principal': '*',
            'effect': 'allow',
            'condition': 'is_account_owner'
        }
    ]

    def is_account_owner(self, request, view, action) -> bool:
        user = view.get_object()
        return request.user == user