
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Relation, FRIEND, NEUTRAL, BLOCKED, REQUEST, OTHER_REQUEST
from accounts.models import User, Profile
# from django.utils.html import format_html
from django.urls import reverse
# from common.templatetags.html_utils import html_list_join, same_arg_redir_list
from common.views import ActionModelView

class RelationView(ActionModelView):
    model = Relation
    app_name = 'relationship'
    
    def detail_view(self):
        return redirect(Profile.objects.get(user=self.object.to_user))
    
    def __init__(self, object = None, from_user = None, to_user = None, request = None, pk = None):
        if request is not None:
            from_user = request.user
        if pk is not None:
            to_user = User.objects.get(pk=pk)
        if from_user is not None and to_user is not None:
            object = Relation.get(from_user=from_user, to_user=to_user)
        super().__init__(object)
        self.object : Relation = object
        
    def reverse_to_userid(self, viewname):
        return reverse(f'{self.app_name}:{viewname}', kwargs={"pk": self.object.to_user.pk})
            
    def get_actions(self, user = None):
        actions = {}
        relation_between = self.object.relation
        if relation_between == BLOCKED:
            actions[self.reverse_to_userid('unblock_user')] = 'unblock'
        else:
            actions[self.reverse_to_userid('block_user')] = 'block'
            if relation_between == NEUTRAL:
                actions[self.reverse_to_userid('send_friend_request')] = 'friend request'
            if relation_between == REQUEST:
                actions[self.reverse_to_userid('unsend_friend_request')] = 'unsend friend request'
            if relation_between == OTHER_REQUEST:
                actions[self.reverse_to_userid('accept_friend_request')] = 'accept friend request'  
                actions[self.reverse_to_userid('deny_friend_request')] = 'deny friend request' 
            if relation_between == FRIEND:
                actions[self.reverse_to_userid('unfriend_user')] = 'unfriend'
        return actions

    def update_relation(self, relation_id : int):
        self.object.update_relation(type=relation_id)
        return self.detail_view()
    