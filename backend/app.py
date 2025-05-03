from database import Base, engine
from flask import Flask
from flask_cors import CORS
from routes import init_routes
from routes.despesas import register_despesa_routes
import models

Base.metadata.create_all(bind=engine)

app = Flask(__name__)
CORS(app)

def init_routes(app):
    register_despesa_routes(app)

    @app.route('/api/ping')
    def ping():
        return {'message': 'API está funcionando!'}

if __name__ == '__main__':
    app.run(debug=True)
