
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Relation, FRIEND, NEUTRAL, BLOCKED, REQUEST, OTHER_REQUEST
from accounts.models import User
from django.utils.html import format_html
from django.urls import reverse
from common.templatetags.html_utils import html_list_join, same_arg_redir_list


class RelationView():
    model = Relation
    
    @staticmethod
    def get_relation_actions(relation_between):
        if relation_between == BLOCKED:
            return { 'relationship:unblock_user' : 'unblock'}
        context = { 'relationship:block_user' : 'block',}
        if relation_between == NEUTRAL:
            context.update({ f'relationship:send_friend_request': 'friend request',})
        if relation_between == REQUEST:
            context.update({f'relationship:unsend_friend_request' : 'unsend friend request',})
        if relation_between == OTHER_REQUEST:
            context.update({
                f'relationship:accept_friend_request':'accept friend request' , 
                f'relationship:deny_friend_request':'deny friend request' , 
                })
        if relation_between == FRIEND:
            context.update({f'relationship:unfriend_user' : 'unfriend' ,})
        return context

    @staticmethod
    @login_required
    def update_relation(request, relation_id : int, pk : int, ):
        to_user = get_object_or_404(User, pk=pk)
        Relation().update_relation(from_user=request.user, to_user=to_user, type=relation_id)
        return redirect(f'relationship:detail')
 
    @staticmethod
    def get_formated_relation_actions(request, other):
        actions = RelationView.get_relation_actions(Relation.relation_between(from_user=request.user, to_user=other))
        return same_arg_redir_list(actions, sep=' | ', args=[other.id])
 
    @login_required
    def send_friend_request(request, pk):
        return RelationView.update_relation(request, REQUEST, pk)

    @login_required
    def unsend_friend_request(request, pk):
        return RelationView.update_relation(request, NEUTRAL, pk)
    
    @login_required
    def unfriend_unser(request, pk):
        return RelationView.update_relation(request, NEUTRAL, pk)

    @login_required
    def accept_friend_request(request, pk):
        return RelationView.update_relation(request, FRIEND, pk)

    @login_required
    def deny_friend_request(request, pk):
        return RelationView.update_relation(request, NEUTRAL, pk)

    @login_required
    def delete_friend(request, pk):
        return RelationView.update_relation(request, NEUTRAL, pk)

    @login_required
    def unblock_user(request, pk):
        return RelationView.update_relation(request, NEUTRAL, pk)

    @login_required
    def block_user(request, pk):
        return RelationView.update_relation(request, BLOCKED, pk)
