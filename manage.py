from app import app
from common.db import db
from models.User import UserModel
from models.Product import ProductModel
from models.Comment import CommentModel
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

"""
https://flask-migrate.readthedocs.io/en/latest/
We use Flask-Migrate to database migrations.
These are commands to flask-migrate
python manage.py db init --> init migrations
python manage.py db migrate --> migrate models
python manage.py db upgrade --> apply changes
python manage.py db --help --> :)
"""


db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
