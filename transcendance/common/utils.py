from django.shortcuts import redirect

def get_context(app_name:str, d = None):
    context = {
        'app_name' : app_name,
    }
    if  d is not None:
        context.update(d)
    return context 

def get_form_context(app_name:str, forms : list, d = None):
    context = get_context(app_name, d)
    if not isinstance(forms, list):
        forms = [forms]
    context.update({'forms':forms})
    return context

def get_table_context(app_name:str, objects : list, field:str, url_to_redir:str, diplay = None, d = None):
    context = get_context(app_name, d)
    context.update({
        'objects': objects,
        'field': field,
        'redir': url_to_redir,
    } )
    if diplay is not None:
        context.update({'display': diplay})
    return context

def get_action_table_context(app_name:str, objects : list, field:str, url_to_redir:str, 
                                            actions : dict, diplay = None, d = None):
    
    context = get_table_context(app_name, objects, field, url_to_redir, diplay, d)
    context.update({
        'actions': actions,
    })
    return context

def get_optional_action_table_context(app_name:str, objects : list, field:str, url_to_redir:str, 
                                            actions : dict, action_cond : bool, diplay = None, d = None):
    
    context = get_action_table_context(app_name, objects, field, url_to_redir, actions, diplay, d)
    context.update({
        'action_cond': action_cond,
    })
    return context

def redir_to(app_name, name):
    return redirect(f'{app_name}:{name}')

def redir_to_index(app_name):
    return redir_to(app_name, 'index')