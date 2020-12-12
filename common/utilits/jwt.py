import jwt
from flask import current_app


def generate_jwt(payload, expiry, secret=None):
    """
    Generate jwt
    :param payload: dict
    :param expiry: datetime
    :param secret: string
    :return: jwt_token
    """
    _payload = {'exp': expiry}
    _payload.update(payload)

    if not secret:
        secret = current_app.config['JWT_SECRET']

    token = jwt.encode(_payload, secret, algorithm='HS256')
    return token.decode()


def verify_jwt(token, secret=None):
    """
    Verify jwt
    :param token: jwt_token
    :param secret: string
    :return: payload: dict
    """
    if not secret:
        secret = current_app.config['JWT_SECRET']

    try:
        payload = jwt.decode(token, secret, algorithm=['HS256'])
    except jwt.PyJWTError:
        payload = None

    return payload
