from relationship.model_view import RelationView, Relation
from relationship.model_view import RelationAppView
from accounts.model_view import ProfileView, Profile, User
from notifications.model_view import NotificationsAppView
from notifications.model_view import NotificationsView, Notification, Invitation, InvitationView
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
    
    if isinstance(object, Notification):
        return NotificationsAppView().get_notif_view(object=object)
        if InvitationView(object=object).object is not None:
            return InvitationView(object=object)
        return NotificationsView(object=object)

def get_apps_topnav_hyperlinks() -> str:
    app_views = [AccountsAppView(), RelationAppView(), NotificationsAppView()]#, EventAppView()]
    return RedirDict().init_app_views_index(app_views=app_views).get_html

def get_apps_sidenav_hyperlinks(user) -> str:
    app_views = [AccountsAppView(), RelationAppView(), NotificationsAppView()]#, EventAppView()]
    for app in app_views:
        app_actions : RedirDict = app.get_app_redirs(user)
        return app_actions.sidenav_format
    return RedirDict().init_app_views_index(app_views=app_views).get_html
        
