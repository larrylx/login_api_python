from flask import request, g
from common.utilits.jwt import verify_jwt


def token_validation():

    g.user_id = None
    g.user_name = None
    g.is_refresh = False

    token = request.headers.get('Authorization')
    if token is not None and token.startswith('Bearer '):

        token = token[7:]

        payload = verify_jwt(token)

        if payload is not None:
            g.user_id = payload.get('user_id')
            g.user_name = payload.get('user_name')
            g.is_refresh = payload.get('is_refresh', False)

    # print(g.user_id)
