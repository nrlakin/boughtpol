#!venv/bin/python

import os
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

if os.path.exists('.env'):
  print("Importing application environment variables...")
  for line in open('.env'):
    var = line.strip().split('=')
    if len(var) == 2:
      os.environ[var[0]] = var[1]

from bought import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db)

@manager.command
def test():
    """ Run the unit tests. """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

manager.add_command("shell", Shell(make_context = make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
