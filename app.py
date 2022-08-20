import os
import sys
import logging

from flask import Flask, Response, render_template, redirect, jsonify
from samsungtvws import SamsungTVWS

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

tv_ip = os.environ.get('TV_IP') or "192.168.1.106"
tv = SamsungTVWS(tv_ip)

@app.route("/api/available.json")
def list_available():
    info = tv.art().available()

    # Remove duplicates
    seen = set()
    info = [x for x in info if x['content_id'] not in seen and (seen.add(x['content_id']) or True)]

    return jsonify(info)

@app.route("/api/select/<content_id>", methods=["POST"])
def set_artwork(content_id):
    tv.art().select_image(content_id)
    return redirect("/")

@app.route("/api/preview/<content_id>.jpg")
def preview(content_id):
    info = tv.art().available()

    thumbnail = tv.art().get_thumbnail(content_id)
    return Response(thumbnail, mimetype='image/jpeg')

