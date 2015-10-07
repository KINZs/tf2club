import requests
from StringIO import StringIO

from flask import Blueprint, request, g, flash, send_file
from app import fanny

from models.user import User

api = Blueprint('api', __name__, url_prefix='/api')

@api.route("/user/<int:id>/avatar")
def api_route_avatar(id):
    key = 'avatar:{}'.format(id)

    if fanny.redis.exists(key):
        buffered = StringIO(fanny.redis.get(key))
    else:
        try:
            data = User.get(User.id == id).get_steam_profile()
        except User.DoesNotExist:
            return "", 404

        try:
            r = requests.get(data.get('avatarfull'))
            r.raise_for_status()
        except Exception:
            return "", 500

        buffered = StringIO(r.content)
        fanny.redis.setex(key, r.content, (60 * 60))

    buffered.seek(0)
    return send_file(buffered, mimetype='image/jpeg')
