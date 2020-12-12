from . import create_flask_app
from flask import jsonify
from common.settings.default import DefaultConfig


app = create_flask_app(DefaultConfig, True, 'LOGIN_GLOBAL_SETTING')


@app.route('/')
def index():
    rules_iterator = app.url_map.iter_rules()
    return jsonify(
        {rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ('route_map', 'static')})
