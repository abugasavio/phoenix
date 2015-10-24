
def get_farm(request):
    try:
        request.user.farm
    except AttributeError:
        return {}
    else:
        return {'farm': request.user.farm}
