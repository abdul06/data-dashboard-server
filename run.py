from api import create_app
import os

env = os.environ.get("CONFIG_ENVIRONMENT")

app = create_app(env)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)