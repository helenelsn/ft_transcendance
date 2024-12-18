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

    def get_app_redirs(self, user : User) -> RedirDict:
        if user.is_authenticated:
            return ProfileView(user).action_dict()
        else:
            ProfileView.unloged_actions()

class ProfileView(ActionModelView):
    
    app_view = AccountsAppView()
    
    @staticmethod
    def unloged_actions() -> RedirDict:
        return RedirDict().add_page_list(['login', 'register'])
    
    def __init__(self, object):
        if isinstance(object, Profile):
            super().__init__(object)
        elif isinstance(object, User):
            super().__init__(object.profile)
        else:
            super().__init__(object.user.profile)
        
    def action_dict(self, index: bool = True, index_display : str = None, edit=True, logout = True) -> RedirDict:
        d = RedirDict()
        if index:
            index_display = f'{self.object.user.username}' if index_display is None else index_display
            d.add_page(app_view=self.app_view, page=('index', index_display), main_key=True)
        if edit:
            self.add_object_actions(actions=('edit', 'edit profile'), d = d)
        if logout:
            d.add_page(app_view=self.app_view, page='logout')
        return d
        
    def get_user_actions_on_obj(self, user : User) -> RedirDict:
        if user == self.object.user:
            return self.action_dict(index_display='my account', logout=False)
        else:
            return RelationView(from_user=self.object.user, to_user=user).get_actions()
            
    @staticmethod
    def get_user(user):
        if isinstance(user, int):
            return User.objects.get(pk=user)
        else:
            return user
     