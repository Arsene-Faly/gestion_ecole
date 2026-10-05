from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

from config import db
from models.academic_year import AcademicYear


academic_year = Blueprint(
    "academic_year",
    __name__,
    url_prefix="/annee_scolaire"
)


# ==========================================
# LISTE DES ANNÉES SCOLAIRES
# ==========================================

@academic_year.route("")
def academic_year_view():

    # Récupérer toutes les années scolaires
    academic_years = AcademicYear.query.order_by(
        AcademicYear.start_date.desc()
    ).all()

    return render_template(
        "pages/academic_year/academic_year_index.html",
        academic_years=academic_years,
        page="academic"
    )


# ==========================================
# ACTIVER UNE ANNÉE SCOLAIRE
# ==========================================

@academic_year.route(
    "/<int:academic_year_id>/activate"
)
def academic_year_activate(academic_year_id):

    # Récupérer l'année scolaire sélectionnée
    academic_year = AcademicYear.query.get_or_404(
        academic_year_id
    )

    # Désactiver toutes les années scolaires
    AcademicYear.query.update({
        AcademicYear.is_active: False
    })

    # Activer l'année sélectionnée
    academic_year.is_active = True

    # Enregistrer les modifications
    db.session.commit()

    # Message de confirmation
    flash(
        f"L'année scolaire {academic_year.name} "
        f"est maintenant active.",
        "success"
    )

    # Retourner vers la liste
    return redirect(
        url_for("academic_year.academic_year_view")
    )