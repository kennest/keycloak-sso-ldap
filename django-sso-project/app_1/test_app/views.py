from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def logout_view(request):
    # Déconnexion côté Django

    logout(request)
    # Redirection vers Keycloak pour logout global
    keycloak_logout_url = (
        "http://localhost:8080/realms/myrealm/protocol/openid-connect/logout"
    )
    redirect_uri = "http://localhost:8000/oidc/authenticate/"
    return redirect(f"{keycloak_logout_url}?redirect_uri={redirect_uri}")


# @login_required
# Create your views here.
def hello_from_app_1(request):
    return render(request, "index.html")
