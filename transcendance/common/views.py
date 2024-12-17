from django.shortcuts import render
from common.templatetags import html_utils
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from abc import ABC, abstractmethod
from accounts.models import User, models

class BaseAppView():
    app_name='app_name'
    # editable = True

    def get_viewname(self, arg : str):
        return f'{self.app_name}:{arg}'

    @property
    def index_viewname(self):
        return self.get_viewname('index')
        
    @property
    def edit_viename(self):
        return self.get_viewname('edit')
    
    def rev(self, viewname='index', object=None):
        args = [object.pk] if object is not None else [] 
        return reverse(self.get_viewname(viewname), args=args)
        
    def get_hyperlink(self, display, viewname='index', object=None):
        html_utils.format_hyperlink(self.rev(viewname=viewname, object=object), display=display)
    

class BasicModelView(ABC):
    app_view=BaseAppView()
    
    def __init__(self, object : models.Model):
        self.object : models.Model = object
        
    def linked_name(self, url):
        return html_utils.format_hyperlink(url, display=self.object.name)
    
    def reverse_objectid(self, viewname):
        return self.app_view.rev(viewname, self.object)
    
    @property
    def detail_linked_name(self):
        return self.linked_name(self.absolute_url)
    
    @property
    def edit_url(self):
        return self.reverse_objectid(self.app_view.edit_viename)
    
    @property
    def absolute_url(self):
        return self.object.get_absolute_url()
    
    def detail_view(self):
        return redirect(self.absolute_url)
    
    def settings_view(self):
        return redirect(self.edit_url)
        
    def index_view(self):
        return redirect(self.app_view.index_viewname)
    
class ActionModelView(BasicModelView):
    @abstractmethod
    def get_actions(self, user : User):
        return {}
    
    def actions_links(self, user = None):
        return html_utils.format_dict_hyperlink_display(redirs=self.get_actions(user), sep=' | ')