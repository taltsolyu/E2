import os
from config import app
from professores.professores_routes import professores_bp

app.register_blueprint(professores_bp)

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )