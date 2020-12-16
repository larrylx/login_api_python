from flask import current_app, g
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from bcrypt import gensalt, hashpw, checkpw
from common.utilits.jwt import generate_jwt
from common.utilits import parser
from common.utilits.decorators import login_required
from common.db import db
from common.db.user import User
from datetime import datetime, timedelta


class Authorization(Resource):

    def _generate_tokens(self, user_id, user_name=None, refresh=True):
        """
        Generate token and refresh_token
        :param user_id: string
        :param refresh: boolean
        :return: token, refresh_token
        """

        # token_secret = current_app.config['JWT_SECRET']
        token_expiry = datetime.utcnow() + timedelta(hours=current_app.config['JWT_EXPIRY_HOURS'])

        token = generate_jwt({'user_id': user_id, 'user_name': user_name}, token_expiry)

        if refresh:
            token_expiry = datetime.utcnow() + timedelta(days=current_app.config['JWT_REFRESH_DAYS'])
            refresh_token = generate_jwt({'user_id': user_id, 'user_name': user_name, 
                                          'is_refresh': True}, token_expiry)
        else:
            refresh_token = None

        return token, refresh_token

    def get(self):
        return {'You sent a get request': 'Your get request has responded',
                'Status is 418': 'I\'m a teapot'}, 418

    def post(self):

        auth_parser = RequestParser()
        auth_parser.add_argument('user_email', type=parser.email, required=True, location='json')
        auth_parser.add_argument('password', required=True, location='json')
        args = auth_parser.parse_args()
        user_email = args.user_email
        password = args.password

        user_target = User.query.filter_by(email=user_email).first()

        # Other search method
        # ret1 = db.session.query(User.name).all()
        # test_query[0][0]
        # ret2 = User.query.all()
        # [row.name for row in ret][0]

        password = password.encode('utf-8')
        passwd_match = False

        if user_target is None:
            passwd_match = passwd_match
        else:
            user_password = user_target.password
            passwd_match = checkpw(password, user_password)

        if passwd_match:
            token, refresh_token = self._generate_tokens(user_target.id, user_target.name)
            return {'token': token, 'refresh_token': refresh_token}, 201
        else:
            return {'message': {'Unauthorized': 'Incorrect Password or User Does not Exist'}}, 401

    def put(self):
        """
        Refresh Token
        :return: token
        """
        if g.user_id is not None and g.is_refresh is True:
            token, refresh_token = self._generate_tokens(g.user_id, g.user_name, refresh=False)
            return {'token': token}
        else:
            return {'message': {'Token': 'Invalid token, redirect to log in page'}}, 403


class Signup(Authorization):

    def get(self):
        return {'You sent a get request': 'Your get request has responded',
                'Status is 418': 'I am a teapot'}, 418

    def post(self):
        auth_parser = RequestParser()
        auth_parser.add_argument('user_email', type=parser.email, required=True, location='json')
        auth_parser.add_argument('password', required=True, location='json')
        auth_parser.add_argument('user_name', required=True, location='json')
        args = auth_parser.parse_args()
        user_email = args.user_email
        password = args.password
        user_name = args.user_name

        user_target = User.query.filter_by(email=user_email).first()

        if user_target is None:
            # snowflake
            user_id = current_app.snowflake.get_id()
            salt = gensalt()
            password = password.encode('utf-8')
            password = hashpw(password, salt)
            user = User(id=user_id, email=user_email, password=password, name=user_name, last_login=datetime.now())
            db.session.add(user)
            db.session.commit()
            token, refresh_token = self._generate_tokens(user_id, user_name)
            return {'token': token, 'refresh_token': refresh_token}, 201

        else:
            return {'message': {'user_email': 'User exist'}}, 400


class Secrettest(Resource):
    """
    A demo view hied by
    """
    method_decorators = [login_required]

    def get(self):
        return {'Success': 'You found me!'}, 200

    def post(self):
        return {'Success': 'You found me!'}, 200
