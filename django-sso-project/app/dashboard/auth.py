from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from django.contrib.auth.models import User


# Ajoutez cette fonction au niveau du module (pas dans la classe)
def verify_claims(claims):
    """
    Fonction de vérification des claims plus permissive pour le débogage
    """
    import logging

    logger = logging.getLogger(__name__)
    logger.debug(f"Vérification des claims externes: {claims}")

    # Vérifier seulement le minimum requis
    required_claims = ["sub"]
    missing_claims = [claim for claim in required_claims if claim not in claims]

    if missing_claims:
        logger.error(f"Claims manquants: {missing_claims}")
        return False

    return True


class KeycloakOIDCAuthenticationBackend(OIDCAuthenticationBackend):
    """
    Authentification backend personnalisé pour Keycloak
    """

    def create_user(self, claims):
        """
        Crée un nouvel utilisateur à partir des claims reçus de Keycloak
        """
        print(f"Creating user with claims: {claims}")
        user = User.objects.create_user(
            username=claims.get("preferred_username", claims.get("sub")),
            email=claims.get("email", ""),
            first_name=claims.get("given_name", ""),
            last_name=claims.get("family_name", ""),
        )

        self.update_user_attributes(user, claims)

        return user

    def update_user(self, user: User, claims):
        """
        Met à jour les informations de l'utilisateur à partir des claims
        """
        print(f"Updating user with claims: {claims}")
        user.email = claims.get("email", "")
        user.first_name = claims.get("given_name", "")
        user.last_name = claims.get("family_name", "")

        self.update_user_attributes(user, claims)

        user.save()

        return user

    def update_user_attributes(self, user: User, claims):
        """
        Met à jour les attributs supplémentaires de l'utilisateur
        """
        print(f"Updating user attributes with claims: {claims}")
        # Gérer les rôles et permissions si nécessaire
        realm_roles = claims.get("realm_access", {}).get("roles", [])

        # Exemple: attribuer le statut de superuser basé sur un rôle spécifique
        if "admin" in realm_roles:
            user.is_staff = True
            user.is_superuser = True
        else:
            user.is_staff = False
            user.is_superuser = False
