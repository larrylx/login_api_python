from flask import Flask

from db import db
from auth import user_auth_bp
from utilits.middlewares import token_validation
from utilits.snowflake import IdWorker


def create_flask_app(config, enable_config_file=False, env_config_file='file_name'):
    app = Flask(__name__)
    app.config.from_object(config)

    if enable_config_file:
        app.config.from_envvar(env_config_file, silent=False)

    # Register Hook
    app.before_request(token_validation)

    # Register User Auth Blue Print
    app.register_blueprint(user_auth_bp)

    # init database
    db.init_app(app)

    # Register Snowflake to app
    app.snowflake = IdWorker(app.config['DATACENTER_ID'],
                             app.config['WORKER_ID'],
                             app.config['SEQUENCE'])

    return app
