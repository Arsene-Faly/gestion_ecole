from config import db

class Level(db.Model):
    
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    # Ajout de ce champs après création table classe
    classes = db.relationship(
        "SchoolClass",
        back_populates="level",
        cascade="all, delete-orphan"
    )