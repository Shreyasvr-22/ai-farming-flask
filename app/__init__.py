from flask import Flask, app
from flask_cors import CORS  # ✅ Import this

def create_app():
    app = Flask("ai_farming_project")
    CORS(app)  # ✅ Enable CORS for all routes

    from .routes import main
    app.register_blueprint(main)git add .
git commit -m "Enable CORS"
git push origin main


    return app
CORS(app, resources={r"/*": {"origins": "http://10.189.250.200:3000"}})
