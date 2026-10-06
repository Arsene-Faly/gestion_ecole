from app import app
from config import db
from models import Level


levels = [
    # Préscolaire
    ("Petite Section", "Premier niveau de l'enseignement préscolaire."),
    ("Moyenne Section", "Deuxième niveau de l'enseignement préscolaire."),
    ("Grande Section", "Dernier niveau de l'enseignement préscolaire."),

    # Primaire
    ("CP", "Première année de l'enseignement primaire."),
    ("CE1", "Deuxième année de l'enseignement primaire."),
    ("CE2", "Troisième année de l'enseignement primaire."),
    ("CM1", "Quatrième année de l'enseignement primaire."),
    ("CM2", "Dernière année de l'enseignement primaire."),

    # Collège
    ("6e", "Première année de l'enseignement secondaire."),
    ("5e", "Deuxième année de l'enseignement secondaire."),
    ("4e", "Troisième année de l'enseignement secondaire."),
    ("3e", "Dernière année du collège."),

    # Lycée
    ("Seconde", "Première année du lycée."),
    ("Première", "Deuxième année du lycée."),
    ("Terminale", "Dernière année du lycée.")
]


with app.app_context():

    for name, description in levels:

        level = Level(
            name=name,
            description=description
        )

        db.session.add(level)

    db.session.commit()

    print("Niveaux scolaires créés avec succès, de la Petite Section à la Terminale.")