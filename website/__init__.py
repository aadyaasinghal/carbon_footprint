from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hello world"
    from .auth import auth
    from .views import views
    app.register_blueprint (auth, url_prefix = "/")
    app.register_blueprint (views, url_prefix = "/")
    print ("HELLO WORLD")
    return app
