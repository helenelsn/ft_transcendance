from django.shortcuts import render
from common.templatetags import html_utils
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from abc import ABC, abstractmethod
from accounts.models import User, models

class BasicModelView(ABC):
    app_name='app_name'
    
    def __init__(self, object : models.Model):
        self.object : models.Model = object
        
    def linked_name(self, url):
        return html_utils.format_hyperlink(url, display=self.object.name)
    
    def reverse_objectid(self, viewname):
        return reverse(viewname, kwargs={"pk": self.object.pk})
    
    @property
    def detail_linked_name(self):
        return self.linked_name(self.absolute_url)
    
    @property
    def edit_url(self):
        return self.reverse_objectid(f"{self.app_name}:edit")
    
    @property
    def absolute_url(self):
        return self.object.get_absolute_url()
    
    def detail_view(self):
        return redirect(self.absolute_url)
    
    def settings_view(self):
        return redirect(self.edit_url)
        
    def index_view(self):
        return redirect(f'{self.app_name}:index')
    
class ActionModelView(BasicModelView):
    @abstractmethod
    def get_actions(self, user : User):
        return {}
    
    def actions_links(self, user = None):
        return html_utils.format_dict_hyperlink_display(redirs=self.get_actions(user), sep=' | ')