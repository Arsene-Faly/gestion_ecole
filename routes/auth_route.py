from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from config import db
from models.user import User

from werkzeug.security import generate_password_hash, check_password_hash

from decorators import role_required, guest_required

auth_route = Blueprint(
    "auth_route",
    __name__,
    url_prefix="/auth"
)


@auth_route.route("/login", methods=["GET", "POST"])
@guest_required
def login_view():

    errors = []

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        # =========================
        # VALIDATION
        # =========================

        if not email:
            errors.append(
                "L'adresse email est obligatoire."
            )

        if not password:
            errors.append(
                "Le mot de passe est obligatoire."
            )

        # =========================
        # CONNEXION
        # =========================

        if not errors:

            user = User.query.filter_by(
                email=email
            ).first()

            if not user:
                errors.append(
                    "Email ou mot de passe incorrect."
                )

            elif not check_password_hash(
                user.password,
                password
            ):
                errors.append(
                    "Email ou mot de passe incorrect."
                )

            else:

                # =========================
                # SESSION
                # =========================

                session["user_id"] = user.id
                session["email"] = user.email
                session["role"] = user.role

                flash(
                    "Connexion réussie.",
                    "success"
                )

                # =========================
                # REDIRECTION
                # =========================

                if user.role == "admin":
                    return redirect(
                        url_for("admin_route.admin_view")
                    )

                return redirect(
                    url_for("main_route.home_view")
                )

    context = {
        "errors": errors,
        "email": request.form.get("email", "")
    }

    return render_template(
        "pages/auth/login.html",
        **context
    )


@auth_route.route("/register", methods=["GET", "POST"])
@guest_required
def register_view():

    errors = []

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        # =========================
        # VALIDATION
        # =========================

        if not email:
            errors.append("L'adresse email est obligatoire.")

        elif "@" not in email:
            errors.append("L'adresse email est invalide.")

        if not password:
            errors.append("Le mot de passe est obligatoire.")

        elif len(password) < 6:
            errors.append(
                "Le mot de passe doit contenir au moins 6 caractères."
            )

        if password != confirm_password:
            errors.append(
                "Les mots de passe ne correspondent pas."
            )

        # =========================
        # VERIFIER EMAIL EXISTANT
        # =========================

        if not errors:

            user = User.query.filter_by(
                email=email
            ).first()

            if user:
                errors.append(
                    "Cette adresse email est déjà utilisée."
                )

        # =========================
        # CREATION USER
        # =========================

        if not errors:

            hashed_password = generate_password_hash(
                password
            )

            user = User(
                email=email,
                password=hashed_password
            )

            db.session.add(user)
            db.session.commit()

            flash(
                "Votre compte a été créé avec succès.",
                "success"
            )

            return redirect(
                url_for("auth_route.login_view")
            )

    context = {
        "errors": errors,
        "email": request.form.get("email", "")
    }

    return render_template(
        "pages/auth/register.html",
        **context
    )
    
@auth_route.route("/logout")
def logout_view():

    session.clear()

    flash(
        "Vous êtes maintenant déconnecté.",
        "success"
    )

    return redirect(
        url_for("main_route.home_view")
    )