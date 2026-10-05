L'année scolaire sert à définir la période scolaire dans laquelle se déroulent les activités de l'école.

## CRUD

--Année Scolaire :

| id | name      | start_date | end_date   | is_active || Actions                              |
| -: | --------- | ---------- | ---------- | --------- || Voir - Modifier - Supprimer - Switch |
|  1 | 2025-2026 | 2025-09-01 | 2026-06-30 | False     || Voir - Modifier - Supprimer - Switch |
|  2 | 2026-2027 | 2026-09-01 | 2027-06-30 | True      || Voir - Modifier - Supprimer - Switch |
|  3 | 2027-2028 | 2027-09-01 | 2028-06-30 | False     || Voir - Modifier - Supprimer - Switch |

## Models Année Scolaire
```py
from config import db

class AcademicYear(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(
        db.String(20),
        nullable=False,
        unique=True
    )

    start_date = db.Column(
        db.Date,
        nullable=False
    )

    end_date = db.Column(
        db.Date,
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    def __repr__(self):
        return f"<AcademicYear {self.name}>"
```

flask --app app db init

flask --app app db migrate -m "Create contact table"
flask --app app db upgrade

### Seed Année Scolaire
```py
from app import app
from config import db
from models import AcademicYear


with app.app_context():

    for year in range(2026, 2030):

        academic_year = AcademicYear(
            name=f"{year}-{year + 1}",
            start_date=f"{year}-09-01",
            end_date=f"{year + 1}-06-30",
            is_active=(year == 2026)
        )

        db.session.add(academic_year)

    db.session.commit()

    print("Années scolaires créées avec succès 2026 jusqu'à 2030.")
```

Validation :

```py
# Vérification des dates
if start_date and end_date:

    if start_date >= end_date:
        errors.append(
            "La date de début doit être avant la date de fin."
        )
```

```html
<form method="POST">

    <div class="form-group">
        <label for="name">Année scolaire</label>
        <input
            type="text"
            id="name"
            name="name"
            placeholder="Ex: 2026-2027"
            required
        >
    </div>

    <div class="form-group">
        <label for="start_date">Date de début</label>
        <input
            type="date"
            id="start_date"
            name="start_date"
            required
        >
    </div>

    <div class="form-group">
        <label for="end_date">Date de fin</label>
        <input
            type="date"
            id="end_date"
            name="end_date"
            required
        >
    </div>

    <button type="submit">
        Enregistrer
    </button>

</form>
```


```py
from flask import redirect, url_for, flash

from config import db
from models import AcademicYear


@admin.route("/academic-year/<int:academic_year_id>/activate")
def academic_year_activate(academic_year_id):

    # Récupérer l'année scolaire sélectionnée
    academic_year = AcademicYear.query.get_or_404(
        academic_year_id
    )

    # Désactiver toutes les années scolaires
    AcademicYear.query.update({
        AcademicYear.is_active: False
    })

    # Activer l'année sélectionnée
    academic_year.is_active = True

    # Enregistrer les modifications
    db.session.commit()

    flash(
        f"L'année scolaire {academic_year.name} est maintenant active.",
        "success"
    )

    return redirect(
        url_for("admin.academic_year_list")
    )
```

## Affichage flash 
```html
{% with messages = get_flashed_messages(with_categories=true) %}

    {% if messages %}

        {% for category, message in messages %}

            <div class="alert alert-{{ category }}">
                {{ message }}
            </div>

        {% endfor %}

    {% endif %}

{% endwith %}
```