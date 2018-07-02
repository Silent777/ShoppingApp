import os
from flask_migrate import Manager, Migrate, MigrateCommand

from models import db
from run import create_app

app = create_app()

app.config.from_object(os.environ.get("config.DevelopmentConfig"))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
