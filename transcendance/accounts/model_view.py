from .models import Profile, User
from common.templatetags import html_utils
from common.views import BasicModelView, ActionModelView
from common.views import BaseAppView, RedirDict
from relationship.model_view import RelationView
from enum import Enum
class AccountsAppView(BaseAppView):
    app_name='accounts'
        
    @property
    def register_viewname(self):
        return self.get_viewname('register')
    
    @property
    def login_viewname(self):
        return self.get_viewname('login')
    
    @property
    def logout_viewname(self):
        return self.get_viewname('logout')

    def get_menu_redirs(self, user) -> dict:
        user_view = ProfileView(user)
        if user.is_authenticated:
            redirs = {
                'accounts:index': f'{user.username}',
                'accounts:logout': 'logout',
            }
        else:
            for page in ['login', 'register']:
                redirs[self.rev(page)] = page,
            redirs[self.rev(self.register_viewname)] = 'register'

class ProfileView(ActionModelView):
    
    app_view = AccountsAppView()
    
    def __init__(self, object):
        if isinstance(object, Profile):
            super().__init__(object)
        elif isinstance(object, User):
            super().__init__(object.profile)
        else:
            super().__init__(object.user.profile)
        
    def get_actions(self, user : User) -> dict:
        if user == self.object.user:
            return {self.edit_url : 'edit'}
        else:
            return RelationView(from_user=self.object.user, to_user=user).get_actions()
        
    @staticmethod
    def get_user(user):
        if isinstance(user, int):
            return User.objects.get(pk=user)
        else:
            return user
     