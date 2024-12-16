from common.const import AppRedir, ACCOUNTS

class AccountsRedirs(AppRedir):
    app_name = ACCOUNTS
    
    @property
    def login(self):
        return self.to_page('login')
    
    @property
    def logout(self):
        return self.to_page('logout')
    
    @property
    def register(self):
        return self.to_page('register')
    
    def detail(self, obj):
        return self.to_page('profil_detail', args=[obj.pk])
    
    def edit(self, obj):
        return self.to_page('edit_profil', args=[obj])
        
    def account_management_actions_dict(self, user):
        actions = {}
        
        if user.is_authenticated:
            actions.update({
                self.logout : 'logout',
                self.detail(user.profile) : user.username,
            })
        else:
            actions.update({
                self.login : 'login',
                self.register : 'register'
            })
        return actions
            