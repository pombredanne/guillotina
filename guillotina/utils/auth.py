from guillotina.interfaces import IPrincipal
from guillotina.interfaces import IRequest


def get_authenticated_user(request: IRequest) -> IPrincipal:
    """
    Get the currently authenticated user
    """
    if (hasattr(request, 'security') and
            hasattr(request.security, 'participations') and
            len(request.security.participations) > 0):
        return request.security.participations[0].principal
    else:
        return None


def get_authenticated_user_id(request: IRequest) -> str:
    """
    Get the currently authenticated user id
    """
    user = get_authenticated_user(request)
    if user:
        return user.id