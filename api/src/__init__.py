from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from src import blueprints
    blueprints.init_app(app) 
    return app