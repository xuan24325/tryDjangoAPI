from django.shortcuts import render


def home(request):
    import requests
    import json
    api_request1 = requests.get("https://api.github.com/users?since=0")
    api1 = json.loads(api_request1.content)
    return render(request, 'home.html', {"api":api1})

def user(request):
    if request.method == 'POST':
        import requests
        import json
        user = request.POST['user']
        user_request1 = requests.get("https://api.github.com/users/"+user)
        username = json.loads(user_request1.content)
        return render(request, 'user.html', {'user':user, 'username':username})
    else:
        notfound = "please use Search..."
        return render(request, 'user.html', {'notfound':notfound})
