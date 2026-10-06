Inscription = Enrollement

```py
from config import db


class Enrollment(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("student.id"),
        nullable=False
    )

    class_id = db.Column(
        db.Integer,
        db.ForeignKey("school_class.id"),
        nullable=False
    )

    academic_year_id = db.Column(
        db.Integer,
        db.ForeignKey("academic_year.id"),
        nullable=False
    )

    enrollment_date = db.Column(
        db.Date,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="active",
        nullable=False
    )

    student = db.relationship(
        "Student",
        back_populates="enrollments"
    )

    school_class = db.relationship(
        "SchoolClass",
        back_populates="enrollments"
    )

    academic_year = db.relationship(
        "AcademicYear",
        back_populates="enrollments"
    )

    def __repr__(self):
        return f"<Enrollment {self.student_id}>"



--Dans Student

enrollments = db.relationship(
        "Enrollment",
        back_populates="student",
        cascade="all, delete-orphan"
    )


--Dans SchoolClass
enrollments = db.relationship(
        "Enrollment",
        back_populates="school_class",
        cascade="all, delete-orphan"
    )

--Dans Academic_year
enrollments = db.relationship(
        "Enrollment",
        back_populates="academic_year",
        cascade="all, delete-orphan"
    )
```