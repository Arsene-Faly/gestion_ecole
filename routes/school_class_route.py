from flask import Blueprint, render_template

from models import SchoolClass


school_class_route = Blueprint(
    "school_class_route",
    __name__,
    url_prefix="/classe"
)


@school_class_route.route("/")
def school_class_view():

    classes = SchoolClass.query.all() 

    context = {
        "page": "class",
        "classes": classes
    }

    return render_template(
        "pages/class/class_index.html",
        **context
    )