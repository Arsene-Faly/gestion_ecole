from flask import Blueprint, render_template

from models import Student


student_route = Blueprint(
    "student_route",
    __name__,
    url_prefix="/eleve"
)


@student_route.route("/")
def student_view():

    students = Student.query.all()

    context = {
        "page": "student",
        "students": students
    }

    return render_template(
        "pages/student/student_index.html",
        **context
    )