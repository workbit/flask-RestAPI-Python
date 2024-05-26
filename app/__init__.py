from flask import Flask
from flask_smorest import Api
from app.config import APIConfig
from app.views.todo import todo

def create_app():
    app = Flask(__name__)
    app.config.from_object(APIConfig)
    
    api = Api(app)
    api.register_blueprint(todo)
    
    return app

