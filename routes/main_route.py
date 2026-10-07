from flask import Blueprint, render_template

main_route = Blueprint("main_route", __name__, url_prefix="")

@main_route.route("/")
def home_view():
    return render_template("pages/home/index.html") 