from . import db


class User(db.Model):
    """
    User basic information From
    """
    __tablename__ = 'user_basic'

    class STATUS:
        ENABLE = 1
        DISABLE = 0

    id = db.Column('user_id', db.Integer, primary_key=True, doc='User ID')
    email = db.Column(db.String, unique=True, nullable=False, doc='User Email')
    status = db.Column(db.Integer, default=1, nullable=False, doc='User Status, 0-Disable，1-Normal')
    password = db.Column(db.LargeBinary, nullable=False, doc='Password')
    name = db.Column('user_name', db.String, nullable=False, doc='User Name')
    profile_photo = db.Column(db.String, doc='Profile Picture')
    last_login = db.Column(db.DateTime, doc='User Last Log in Time')