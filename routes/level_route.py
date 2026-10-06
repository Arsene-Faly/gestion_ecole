from flask import Blueprint, render_template

from models import Level


level_route = Blueprint(
    "level_route",
    __name__,
    url_prefix="/niveau"
)


@level_route.route("/")
def level_view():

    levels = Level.query.all()

    context = {
        "page": "level",
        "levels": levels
    }

    return render_template(
        "pages/level/level_index.html",
        **context
    )


@level_route.route("/<int:id>")
def level_detail(id):

    level = Level.query.get_or_404(id)

    context = {
        "page": "level",
        "level": level
    }

    return render_template(
        "pages/level/level_detail.html",
        **context
    )