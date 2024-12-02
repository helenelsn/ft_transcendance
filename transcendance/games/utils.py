def game_context(d = None):
    context={
        'app_name' : 'games'
    }
    if d is not None:
        context.update(d)
    return context