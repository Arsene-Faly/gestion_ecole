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