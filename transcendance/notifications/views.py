from django.shortcuts import render

app_name = 'notifications'

# Create your views here.
def index(request):
    # context = {
    #     'objects': User.objects.all(),
    #     'field': 'username',
    #     'redir': 'accounts:profile_page',
    #     'action_cond': request.user.is_authenticated,
    #     'actions':{'friend' : f'relationship:send_friend_request', 'block' : f'relationship:block_user'},
    # }
    print(f'{app_name}/index.html')
    return render(request, f'{app_name}/index.html', {})
