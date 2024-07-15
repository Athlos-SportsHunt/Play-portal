from django.shortcuts import render
from json import dumps
# Create your views here.
def index(request):
    return render(request, "index.html")

def profile(request):
    user = request.user
    auth0_user = user.social_auth.get(provider="auth0")

    user_data = {
        "user_id": auth0_user.uid,
        # "name": auth0_user.first_name,
        "picture": auth0_user.extra_data["picture"],
    }

    context = {
        "auth0_user": auth0_user,
        "user_data": dumps(user_data, indent=4),
    }
    return render(request, "profile.html", context) 