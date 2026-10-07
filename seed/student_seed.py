from datetime import date

from faker import Faker

from app import app
from config import db
from models import Student


fake = Faker("fr_FR")


with app.app_context():

    for _ in range(50):

        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            date_of_birth=fake.date_of_birth(
                minimum_age=6,
                maximum_age=20
            ),
            gender=fake.random_element(
                elements=[
                    "Masculin",
                    "Féminin"
                ]
            ),
            address=fake.address(),
            phone=fake.phone_number()
        )

        db.session.add(student)

    db.session.commit()

    print("50 étudiants créés avec succès.")