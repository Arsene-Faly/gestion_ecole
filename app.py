from flask import Flask
from flask_migrate import Migrate

from config import Config, db

from flask import Flask

# models
from models import AcademicYear, Level, SchoolClass

from routes import admin_route, academic_year, level_route, school_class_route

app = Flask(__name__)

# Configuration
app.config.from_object(Config)

# Initialisation de SQLAlchemy
db.init_app(app)

# Initialisation de Flask-Migrate
migrate = Migrate(app, db)

# Enregistrer
app.register_blueprint(admin_route)
app.register_blueprint(academic_year)
app.register_blueprint(level_route)
app.register_blueprint(school_class_route)

# Si notre fichier est executer notre serveur marche
if __name__ == "__main__":
    app.run(debug=True, port=5000)

