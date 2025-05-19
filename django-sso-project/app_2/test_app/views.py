from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest


def logout_view(request):
    # Déconnexion côté Django

    logout(request)
    # Redirection vers Keycloak pour logout global
    keycloak_logout_url = (
        "http://localhost:8080/realms/myrealm/protocol/openid-connect/logout"
    )
    redirect_uri = "http://localhost:8001/oidc/authenticate/"
    return redirect(f"{keycloak_logout_url}?redirect_uri={redirect_uri}")


@login_required
# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        user = request.user
    else:
        user = None
    return render(request, "index.html", {"user": user})
