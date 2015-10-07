import json

from flask import Flask, request, g, flash, send_from_directory

from fannypack.app import FannyPack
from fannypack.session import Session
from flask.ext.openid import OpenID
from steamy import SteamAPI

import db

from models.user import User

app = Flask("club")
app.config.from_pyfile("settings.py")

fanny = FannyPack(app, auto_load_views=False)
oid = OpenID(app)

steam = SteamAPI(app.config.get("STEAM_API_KEY"))

@app.route('/static/template/<path:path>')
def send_js_templates(path):
    return send_from_directory('templates/js', path)

@app.before_request
def app_before_request():
    if '/static/' in request.path:
        return

    g.session = app.sessions.get()
    g.uid = g.session.get('u')

    if g.uid:
        g.user = User.get(id=g.uid)
    else:
        g.user = None

@app.after_request
def app_after_request(response):
    if '/static/' in request.path:
        return response

    if g.user:
        g.session['u'] = g.user.id if isinstance(g.user, User) else g.uid
        g.session.save(response)
    else:
        g.session.delete()

    return response

@app.template_filter("json")
def jsonify_filter(x):
    return json.dumps(x, separators=(',', ':'))
