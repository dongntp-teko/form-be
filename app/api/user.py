from app.services import user
from app.extensions.namespace import Namespace
import flask_restplus as _fr
from app.models import User, db
from flask import request

ns = Namespace('users', description='User operations')


@ns.route('/')
class UsersList(_fr.Resource):
    def get(self):
        users = [u.to_dict() for u in user.get_all()]
        return users

    # @ns.expect()
    def post(self):

        email = request.json['email']
        password = request.json['password']
        username = request.json['username']
        # status = request.json['status']


        _user = User(
            email=email,
            password_hash=password,
            username=username
        )
        db.session.add(_user)
        db.session.commit()
        return {
            'status': 'ok'
        }


@ns.route('/<string:id>')
class Users(_fr.Resource):
    def get(self,id):
        return user.User.query.filter_by(id=id).first().to_dict()