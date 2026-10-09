import os
import uuid

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    current_app
)

from werkzeug.utils import secure_filename

from config import db
from decorators import role_required
from models import User, UserProfile
from utils import validate_photo


# Création du Blueprint pour la gestion du profil
profile_route = Blueprint(
    "profile_route",
    __name__,
    url_prefix="/profile"
)


# ==========================================
# AFFICHER LE PROFIL DE L'UTILISATEUR
# ==========================================
@profile_route.route("/")
@role_required("admin", "user")
def profile_view():

    # Récupérer l'utilisateur connecté grâce à la session
    user = User.query.get(session.get("user_id"))

    # Vérifier si l'utilisateur existe
    if user is None:
        flash("Utilisateur introuvable.", "error")
        return redirect(url_for("auth_route.login_view"))

    # Préparer les données à envoyer au template
    context = {
        "user": user
    }

    # Afficher la page du profil
    return render_template(
        "pages/profile/index.html",
        **context
    )


# ==========================================
# MODIFIER LE PROFIL DE L'UTILISATEUR
# ==========================================
@profile_route.route("/modifier", methods=["GET", "POST"])
@role_required("admin", "user")
def profile_edit():

    # Liste des erreurs de validation
    errors = []

    # Récupérer l'utilisateur connecté
    user = User.query.get(session.get("user_id"))

    # Vérifier si l'utilisateur existe
    if user is None:
        flash("Utilisateur introuvable.", "error")
        return redirect(url_for("auth_route.login_view"))

    # Récupérer le profil associé à cet utilisateur
    # Si aucun profil n'existe, profile vaudra None
    profile = UserProfile.query.filter_by(
        user_id=user.id
    ).first()

    # Vérifier si le formulaire a été envoyé
    if request.method == "POST":

        # Récupérer les valeurs saisies dans le formulaire
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        address = request.form.get("address", "").strip()

        # Récupérer le fichier photo envoyé
        photo = request.files.get("photo")

        # ------------------------------------------
        # VALIDATION DES DONNÉES
        # ------------------------------------------

        # Vérifier que le nom complet est renseigné
        if not name:
            errors.append(
                "Le nom complet est obligatoire."
            )

        # Vérifier la photo avec la fonction externe
        # La fonction retourne un message si elle détecte une erreur
        photo_error = validate_photo(photo)

        if photo_error:
            errors.append(photo_error)

        # ------------------------------------------
        # ENREGISTREMENT DES DONNÉES
        # ------------------------------------------

        # Enregistrer uniquement si aucune erreur n'existe
        if not errors:

            # Variable qui contiendra le nom de la nouvelle photo
            new_photo = None

            # Vérifier si une nouvelle photo a été envoyée
            if photo and photo.filename:

                # Récupérer et sécuriser l'extension du fichier
                extension = secure_filename(
                    photo.filename.rsplit(".", 1)[1].lower()
                )

                # Générer un nom de fichier unique
                filename = f"{uuid.uuid4().hex}.{extension}"

                # Définir le dossier de destination des photos
                upload_folder = os.path.join(
                    current_app.static_folder,
                    "uploads"
                )

                # Créer le dossier s'il n'existe pas
                os.makedirs(
                    upload_folder,
                    exist_ok=True
                )

                # Enregistrer physiquement la photo dans le dossier
                photo.save(
                    os.path.join(upload_folder, filename)
                )

                # Conserver le nom du fichier pour la base de données
                new_photo = filename

            # ------------------------------------------
            # CRÉATION DU PROFIL SI INEXISTANT
            # ------------------------------------------
            if profile is None:

                # Créer un nouveau profil lié à l'utilisateur connecté
                profile = UserProfile(
                    user_id=user.id,
                    name=name,
                    phone=phone or None,
                    address=address or None,
                    photo=new_photo or "default.png"
                )

                # Ajouter le nouveau profil à la session SQLAlchemy
                db.session.add(profile)

            else:

                # Mettre à jour les informations du profil existant
                profile.name = name
                profile.phone = phone or None
                profile.address = address or None

                # Remplacer la photo uniquement si une nouvelle est envoyée
                if new_photo:
                    profile.photo = new_photo

            # Enregistrer les modifications dans la base de données
            db.session.commit()

            # Afficher un message de confirmation
            flash(
                "Votre profil a été modifié avec succès.",
                "success"
            )

            # Rediriger vers la page du profil
            return redirect(
                url_for("profile_route.profile_view")
            )

    # ------------------------------------------
    # PRÉPARER LES DONNÉES DU TEMPLATE
    # ------------------------------------------
    context = {
        # Informations de l'utilisateur connecté
        "user": user,

        # Profil existant ou None
        "profile": profile,

        # Liste des erreurs de validation
        "errors": errors,

        # Conserver le nom saisi si le formulaire est invalide
        "name": request.form.get(
            "name",
            profile.name if profile else ""
        ),

        # Conserver le téléphone saisi  
        "phone": request.form.get(
            "phone",
            profile.phone if profile else ""
        ),

        # Conserver l'adresse saisie
        "address": request.form.get(
            "address",
            profile.address if profile else ""
        )
    }                                                                                                                                                                                                                                                                                                                                        

    # Afficher le formulaire de modification avec les données
    return render_template(
        "pages/profile/edit.html",
        **context
    )

