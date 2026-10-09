from config import db

class UserProfile(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(255), nullable=True)

    # Photo de profil
    photo = db.Column(
        db.String(255),
        nullable=True,
        default="default.png"
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False,
        unique=True
    )

    user = db.relationship(
        "User",
        back_populates="profile"
    )