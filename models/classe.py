from config import db


class SchoolClass(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    level_id = db.Column(
        db.Integer,
        db.ForeignKey("level.id"),
        nullable=False
    )

    level = db.relationship(
        "Level",
        back_populates="classes"
    )