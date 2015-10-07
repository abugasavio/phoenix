from phoenix.users.models import User


def get_farm(request):
    try:
        request.user.name
    except AttributeError:
        return {}
    else:
        return {'farm': request.user.name}
