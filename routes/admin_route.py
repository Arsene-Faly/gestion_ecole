from flask import Blueprint, render_template

from decorators import role_required, guest_required

admin_route = Blueprint("admin_route", __name__, url_prefix="/dashboard")

@admin_route.route("/")
# @role_required("admin", "user")
def admin_view():
    context = {
        "page" : "home"
    }
    return render_template("pages/index.html", **context)