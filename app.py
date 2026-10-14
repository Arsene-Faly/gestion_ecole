from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from config import Config, db

from flask import Flask

# models
from models import AcademicYear, Level, SchoolClass, User, Student, UserProfile

from routes import admin_route, academic_year, level_route, school_class_route, main_route, auth_route, student_route, profile_route
 
app = Flask(__name__)

# Configuration
app.config.from_object(Config)

# Initialisation de SQLAlchemy
db.init_app(app)

# Initialisation de Flask-Migrate
migrate = Migrate(app, db)

# Activation de la protection CSRF
csrf = CSRFProtect(app)

# Protection anti-clickjacking
@app.after_request
def security_headers(response):
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = (
        "frame-ancestors 'none'"
    )
    return response

# Enregistrer
app.register_blueprint(admin_route)
app.register_blueprint(academic_year)
app.register_blueprint(level_route)
app.register_blueprint(school_class_route)
app.register_blueprint(main_route)
app.register_blueprint(auth_route)
app.register_blueprint(student_route)
app.register_blueprint(profile_route)

# Si notre fichier est executer notre serveur marche
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

