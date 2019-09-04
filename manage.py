import app
from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role,Review
from  flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CSRFProtect # add csrf protection without creating a FlaskForm
from app import config

import config
import os

# Creating app instance
app = create_app('development')
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(testsg)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role=Role )
if __name__ == '__main__':
    manager.run()
