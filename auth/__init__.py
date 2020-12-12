from flask import Blueprint
from flask_restful import Api

from . import auth
from utilits.output_json import output_json

user_auth_bp = Blueprint('Auth', __name__, url_prefix='/auth')
user_auth_api = Api(user_auth_bp, catch_all_404s=True)
user_auth_api.representation('application/json')(output_json)

user_auth_api.add_resource(auth.Authorization, '/login', endpoint='User_Login')

user_auth_api.add_resource(auth.Signup, '/signup', endpoint='User_Signup')

user_auth_api.add_resource(auth.Secrettest, '/test', endpoint='User_Secret')
