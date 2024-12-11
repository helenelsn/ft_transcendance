# from enum import StrEnum
from django.shortcuts import redirect
from django.urls import reverse


ACCOUNTS ='accounts'
RELATIONS ='relationship'
NOTIFICATIONS ='notifications'
GAMES ='games'


class AppRedir():
    
    def __init__(self, as_redir=False):
        self.as_redir = as_redir
    
    @property
    def index_path(self):
        return f'{self.app_name}:index'
    
    def to_index(self):
        return self.to_page(self.index_path)

    def to_page(self, page, args=None, kwargs=None):
        rev = reverse(f'{self.app_name}:{page}', args=args, kwargs=kwargs)
        if self.as_redir:
            return redirect(rev)
        return rev
            


