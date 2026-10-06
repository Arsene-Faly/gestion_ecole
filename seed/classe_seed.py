from app import app
from config import db
from models import Level, SchoolClass

classes_by_level = {
    "Petite Section": ["A", "B"],
    "Moyenne Section": ["A", "B"],
    "Grande Section": ["A", "B"],

    "CP": ["A", "B"],
    "CE1": ["A", "B"],
    "CE2": ["A", "B"],
    "CM1": ["A", "B"],
    "CM2": ["A", "B"],

    "6e": ["A", "B", "C"],
    "5e": ["A", "B", "C"],
    "4e": ["A", "B", "C"],
    "3e": ["A", "B", "C"],

    "Seconde": ["A", "B", "C"],
    "Première": ["A", "B", "C"],
    "Terminale": ["A", "B", "C", "D"],
}


with app.app_context():

    for level_name, class_names in classes_by_level.items():

        level = Level.query.filter_by(
            name=level_name
        ).first()

        if not level:
            print(f"Niveau introuvable : {level_name}")
            continue

        for class_name in class_names:

            school_class = SchoolClass(
                name=f"{level.name} {class_name}",
                level=level
            )

            db.session.add(school_class)

    db.session.commit()

    print("Classes créées avec succès.")