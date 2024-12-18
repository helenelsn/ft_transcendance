from django.shortcuts import render
from common.templatetags import html_utils
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from abc import ABC, abstractmethod
from accounts.models import User, models

class RedirDict():
    def __init__(self, d = None):
        
        self.dict = {}
        self.add_dict(d)
        self.main_keys = []

    def add(self, url, display):
        self.dict[url] = display
        return self
        
    def add_dict(self, d):
        if isinstance(d, dict):
            self.dict.update(d)
        elif isinstance(d, RedirDict):
            self.dict.update(d.dict.copy())
        return self
        
    def add_page(self, app_view, page, main_key=False):
        if isinstance(page, tuple):
            key, val = page[0], page[1]
        else:
            key, val = page, page
        key = app_view.rev(key)
        if main_key:
            self.main_keys.append(key)
        self.dict[key] = val
        return self
        
    def add_page_list(self, app_view, pages : list):
        for page in pages:
            self.add_page(app_view, page)
        return self
            
    def init_app_views_index(self, app_views):
        for app in app_views:
            self.dict[app.rev(viewname='index')] = app.index_display
        return self
            
    def get_hyperlink(self, page) -> str:
        return html_utils.format_hyperlink(link=page, display=self.dict[page])
            
    @property
    def get(self):
        return self.dict
    
    @property
    def get_html(self):
        return html_utils.html_list_join([self.get_hyperlink(page) for page in self.dict])
    
    @property
    def html_one_line(self):
        return html_utils.html_list_join([self.get_hyperlink(page) for page in self.dict], sep=' | ')
        
    @property
    def sidenav_format(self):
        lst = [self.get_hyperlink(page) for page in self.dict if page in self.main_keys]
        lst.extend([self.get_hyperlink(page) for page in self.dict if page not in self.main_keys])
        return html_utils.html_list_join(lst)
        
    def __str__(self):
        return str(self.dict)

class BaseAppView(ABC):
    app_name='app_name'

    def get_viewname(self, arg : str) -> str:
        return f'{self.app_name}:{arg}'

    @property
    def index_display(self):
        return self.app_name

    @property
    def index_viewname(self) -> str:
        return self.get_viewname('index')
        
    @property
    def edit_viename(self) -> str:
        return self.get_viewname('edit')
    
    def rev(self, viewname='index', object=None) -> str:
        args = [object.pk] if object is not None else []
        return reverse(self.get_viewname(viewname), args=args)
        
    def get_app_redirs(self, user) -> RedirDict:
        return RedirDict()
    
    
class BasicModelView(ABC):
    app_view=BaseAppView()
    
    def add_object_actions(self, actions, object = None, d : RedirDict = None, ) -> RedirDict:
        if d is None:
            d = RedirDict()
        if not isinstance(actions, list):
            actions = [actions]
        for action in actions:
            if not isinstance(action, tuple):
                action = (action, action)
            d.add(self.reverse_objectid(action[0], object), action[1])
        return d
    
    def __init__(self, object : models.Model):
        self.object : models.Model = object
        
    def linked_name(self, url):
        return html_utils.format_hyperlink(url, display=self.object.name)
    
    def reverse_objectid(self, viewname, object = None):
        if object is None :
            object = self.object
        return self.app_view.rev(viewname, object)
    
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
    def get_user_actions_on_obj(self, user : User) -> RedirDict:
        return RedirDict()
    
    def col_actions_links(self, user = None):
        return self.get_user_actions_on_obj(user).html_one_line