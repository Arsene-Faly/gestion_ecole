from config import db

class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    email = db.Column(
        db.String(255),
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.String(50),
        nullable=False,
        default="user"
    )
    
    # Relation avec UserProfile
    profile = db.relationship(
        "UserProfile",
        back_populates="user",
        # Pas de Liste
        uselist=False,
        cascade="all, delete"
    )