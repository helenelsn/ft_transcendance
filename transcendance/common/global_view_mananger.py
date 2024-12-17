from relationship.model_view import RelationView, Relation
from relationship.model_view import RelationAppView
from accounts.model_view import ProfileView, Profile, User
from notifications.model_view import NotificationsAppView
from notifications.model_view import NotificationsView
from accounts.model_view import AccountsAppView
from event.model_view import EventAppView

from .views import BasicModelView
from .views import BaseAppView, RedirDict
from common.templatetags import html_utils

def get_view(object ) -> BasicModelView:
    if isinstance(object, Relation):
        return RelationView(object=object)
    if isinstance(object, User) or isinstance(object, Profile):
        return ProfileView(object)

def get_app_views_index_hyperlinks():
    
    app_views = [AccountsAppView(), RelationAppView(), NotificationsAppView()]#, EventAppView()]
    return RedirDict().init_app_views_index(app_views=app_views).get_html
        
