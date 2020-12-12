from flask import g


def login_required(func):

    def wrapper(*args, **kwargs):

        if g.user_id is not None and g.is_refresh is False:

            return func(*args, **kwargs)

        else:

            return {'message': {'Token': 'Invalid token, redirect to log in page'}}, 401

    return wrapper
