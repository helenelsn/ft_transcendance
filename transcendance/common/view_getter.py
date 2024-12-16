from relationship.model_view import RelationView, Relation
from accounts.model_view import ProfileView, Profile, User
from .views import BasicModelView

def get_view(object ) -> BasicModelView:
    if isinstance(object, Relation):
        return RelationView(object=object)
    if isinstance(object, User) or isinstance(object, Profile):
        return ProfileView(object)