import re

from flask import Blueprint, g, flash, redirect
from fannypack.util import flashy
from app import oid, steam

from models.user import User

auth = Blueprint("auth", __name__, url_prefix="/auth")

steam_id_re = re.compile('steamcommunity.com/openid/id/(.*?)$')

@auth.route("/login")
@oid.loginhandler
def route_auth_login():
    if g.user:
        return redirect(oid.get_next_url())

    return oid.try_login("http://steamcommunity.com/openid")

@auth.route("/logout")
def route_auth_logout():
    g.user = None
    return flashy("You have been logged out")

@oid.after_login
def create_or_login(resp):
    id = steam_id_re.findall(resp.identity_url)[0]

    g.user, new = User.get_or_create(steamid=id)

    profile = g.user.get_steam_profile()
    g.user.nickname = profile['personaname']
    g.user.save()

    if new:
        flash("Welcome to TF2 Club!")
        return redirect("/?onboard=1")

    return redirect(oid.get_next_url())


