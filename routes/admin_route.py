from flask import Blueprint, render_template

from decorators import role_required
from models import Level, SchoolClass

admin_route = Blueprint(
    "admin_route",
    __name__,
    url_prefix="/dashboard"
)


@admin_route.route("/")
@role_required("admin", "user")
def admin_view():

    # Compter les niveaux
    total_levels = Level.query.count()

    # Compter toutes les classes
    total_classes = SchoolClass.query.count()

    # Récupérer tous les niveaux
    levels = Level.query.all()

    # Compter les classes de chaque niveau
    statistiques = []

    for level in levels:
        statistiques.append({
            "name": level.name,
            "value": len(level.classes)
        })

    # Préparer les données à envoyer au template
    context = {
        "page": "home",
        "total_levels": total_levels,
        "total_classes": total_classes,
        "statistiques": statistiques
    }

    return render_template("pages/index.html", **context)
