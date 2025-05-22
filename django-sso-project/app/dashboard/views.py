from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
import json


def oidc_group_required(group_name):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            groups = request.session.get("oidc_userinfo", {}).get("groups", [])
            print(f"User groups: {groups}")  # Debugging line to check user groups
            if group_name in groups:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You are not authorized.")

        return _wrapped_view

    return decorator


def home(request):
    """
    Vue publique accessible à tous les utilisateurs
    """
    return render(
        request,
        "dashboard/home.html",
        {
            "page_title": "Accueil - Vue Publique",
        },
    )


@oidc_group_required("admin")
def dashboard(request):
    """
    Vue privée accessible uniquement aux utilisateurs authentifiés
    """
    user_info = {
        "username": request.user.username,
        "email": request.user.email,
        "full_name": f"{request.user.first_name} {request.user.last_name}",
        "is_superuser": request.user.is_superuser,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "page_title": "Tableau de bord - Vue Privée",
            "user_info": user_info,
        },
    )


@login_required
def user_profile(request):
    """
    Vue pour afficher le profil de l'utilisateur
    """
    return render(
        request,
        "dashboard/profile.html",
        {
            "page_title": "Mon Profil",
        },
    )


@login_required
def user_info_api(request):
    """
    API pour récupérer les informations de l'utilisateur au format JSON
    """
    user_data = {
        "id": request.user.id,
        "username": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "is_staff": request.user.is_staff,
        "is_superuser": request.user.is_superuser,
        "is_authenticated": request.user.is_authenticated,
    }

    return JsonResponse(user_data)
