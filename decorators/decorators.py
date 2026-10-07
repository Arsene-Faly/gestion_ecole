from functools import wraps

from flask import session, redirect, url_for, flash

# Si connecté on peut pas entrer dans login et register
def guest_required(view):

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        # Si déjà connecté
        if session.get("user_id"):

            return redirect(
                url_for("main_route.home_view")
            )

        return view(*args, **kwargs)

    return wrapped_view

# pour les pages protégées
def role_required(*roles):

    def decorator(view):

        @wraps(view)
        def wrapped_view(*args, **kwargs):

            # Pas connecté
            if not session.get("user_id"):
                flash(
                    "Vous devez être connecté.",
                    "warning"
                )

                return redirect(
                    url_for("auth_route.login_view")
                )

            # Récupérer le rôle
            user_role = session.get("role")

            # Vérifier le rôle
            if user_role not in roles:

                flash(
                    "Vous n'avez pas accès à cette page.",
                    "error"
                )

                return redirect(
                    url_for("main_route.home_view")
                )

            return view(*args, **kwargs)

        return wrapped_view

    return decorator