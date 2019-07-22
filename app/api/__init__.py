
from flask import Blueprint
from flask_restplus import Api
from .user import ns as user_ns


api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    app=api_bp,
    version='1.0',
    title='Boilerplate API',
    validate=False,
    # doc='' # disable Swagger UI
)


def init_app(app, **kwargs):
    """
    :param flask.Flask app: the app
    :param kwargs:
    :return:
    """
    api.add_namespace(user_ns)
    app.register_blueprint(api_bp)