def auth_context(request):
    """
    Contexte d'authentification pour les templates
    """
    return {
        "is_authenticated": request.user.is_authenticated,
        "user": request.user if request.user.is_authenticated else None,
    }
