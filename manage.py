import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.app import create_app, db
from src.models.user import User
from src.models.branch import Branch
from src.models.bank import Bank

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

migrate = Migrate()
migrate.init_app(app, db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
