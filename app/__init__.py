from flask import Flask
from flask_cors import CORS  # ✅ Import this

def create_app():
    app = Flask(__name__)
    CORS(app)  # ✅ Enable CORS for all routes

    from .routes import main
    app.register_blueprint(main)

    return app
CORS(app, resources={r"/*": {"origins": "http://10.189.250.200:3000"}})
