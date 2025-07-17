# from flask import Flask
# from dotenv import load_dotenv
# import os

# load_dotenv()

# def create_app():
#     app = Flask(__name__)
#     app.secret_key = os.getenv('SECRET_KEY', 'defaultsecret')

#     # Register Blueprints
#     from app.controllers.main_controller import main_bp
#     app.register_blueprint(main_bp)

#     from app.controllers.admin_controller import admin_bp
#     app.register_blueprint(admin_bp)

#     from app.controllers.projectManagers_controller import projectManagers_bp
#     app.register_blueprint(projectManagers_bp)

#     from app.controllers.teamMembers_controller import teamMembers_bp
#     app.register_blueprint(teamMembers_bp)

#     return app
