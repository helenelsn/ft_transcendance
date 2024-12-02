def accounts_context(d = None):
    context = {
        'app_name' : 'accounts',
    }
    if  d is not None:
        context.update(d)
        # context.join(d)
    return context 