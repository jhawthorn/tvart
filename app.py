import os
import sys
import logging

from flask import Flask, Response, render_template, redirect, jsonify, request
from samsungtvws import SamsungTVWS

logging.basicConfig(level=logging.INFO)

app = Flask(__name__,
        static_url_path="/",
        static_folder='build'
        )

tv_ip = os.environ.get('TV_IP') or "192.168.1.106"
tv = SamsungTVWS(tv_ip)

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/api/available.json")
def list_available():
    art = tv.art()
    available = art.available()
    available.sort(key=lambda x: x["image_date"])
    available.reverse()

    current = art.get_current()["content_id"]

    # Remove duplicates
    seen = set()
    available = [x for x in available if x['content_id'] not in seen and (seen.add(x['content_id']) or True)]

    for art in available:
        art["selected"] = (art['content_id'] == current)

    return jsonify(available)

@app.route("/api/select/<content_id>", methods=["POST"])
def set_artwork(content_id):
    tv.art().select_image(content_id)
    return jsonify({"success": True})

@app.route("/api/delete/<content_id>", methods=["POST"])
def delete_artwork(content_id):
    tv.art().delete(content_id)
    return jsonify({"success": True})

@app.route("/api/preview/<content_id>.jpg")
def preview(content_id):
    info = tv.art().available()

    thumbnail = tv.art().get_thumbnail(content_id)
    return Response(thumbnail, mimetype='image/jpeg')

@app.route("/api/upload", methods=["POST"])
def upload():
    file = request.files['image']
    filename = file.filename

    ext = filename.rsplit('.', 1)[1].lower()
    filetype = "png" if ext == "png" else "jpg"

    data = file.read()

    tv.art().upload(data, file_type=filetype)

    return redirect("/")

