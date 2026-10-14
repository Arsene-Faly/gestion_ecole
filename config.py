# pip install flask-sqlalchemy
# pip install Flask-Migrate
# pip install pymysql

# Im porter SQLAlchemy pour gérer la base de données

import os
from flask_sqlalchemy import SQLAlchemy


# Créer l'objet SQLAlchemy
# Cet objet permettra de créer et manipuler les tables
db = SQLAlchemy()


# Informations de connexion à MySQL
DB_USER = "Arsene"
DB_PASSWORD = "Arsene123"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "my_ecole"


# Classe contenant la configuration de notre application Flask
class Config:

    # Clé secrète utilisée par Flask pour les sessions # et les messages flash 
    # Clé aleatoire longue
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "cle-secrete-temporaire-a-remplacer"
    )
    # Adresse de connexion à la base de données MySQL
    #
    # mysql+pymysql:// signifie :
    # - mysql : nous utilisons MySQL
    # - pymysql : pilote Python utilisé pour communiquer avec MySQL
    #
    # Format :
    # mysql+pymysql://utilisateur:mot_de_passe@hote:port/base_de_donnees

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Désactiver le suivi automatique des modifications
    # Cela évite des traitements inutiles
    SQLALCHEMY_TRACK_MODIFICATIONS = False

