from flask import Blueprint, render_template, g

public = Blueprint('public', __name__)

@public.route("/")
def route_public_index():
    return render_template("base.html")
