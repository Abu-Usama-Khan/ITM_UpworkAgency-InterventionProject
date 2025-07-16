from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY', 'defaultsecret')

    from app.controllers.main_controller import main_bp
    app.register_blueprint(main_bp)

    return app
