#!venv/bin/python
import os

if os.path.exists('.env'):
  print("Importing application environment variables...")
  for line in open('.env'):
    var = line.strip().split('=')
    if len(var) == 2:
      os.environ[var[0]] = var[1]

# wait on import until env vars are populated
from voltus import create_app
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run()
