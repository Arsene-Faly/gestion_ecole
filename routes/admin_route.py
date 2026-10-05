from flask import Blueprint, render_template

admin_route = Blueprint("admin_route", __name__, url_prefix="")

@admin_route.route("/")
def admin_view():
    context = {
        "page" : "home"
    }
    return render_template("pages/index.html", **context)