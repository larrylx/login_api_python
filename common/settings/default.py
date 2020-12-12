class DefaultConfig(object):

    # MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/login'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # JWT
    JWT_SECRET = 'JWT_SECRET'
    JWT_EXPIRY_HOURS = 12
    JWT_REFRESH_DAYS = 14

    # Snowflake
    DATACENTER_ID = 0
    WORKER_ID = 0
    SEQUENCE = 0
