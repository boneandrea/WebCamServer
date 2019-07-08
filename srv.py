# -*- coding: utf-8

from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import picamera
import time
import uuid
import os
import s3


load_dotenv()
width = float(os.environ["IMAGE_WIDTH"])
height = float(os.environ["IMAGE_HEIGHT"])
rotation = int(os.environ["ROTATION"])

TEMPFILE = "img/abc.jpg"
BUCKET = os.environ["BUCKET"]

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html', title='Home')


@app.route('/shot')
def my_shot():

    with picamera.PiCamera() as camera:
        print("start to capture")
        camera.rotation = rotation
        camera.capture(TEMPFILE)
        print("shot")

        put_filename = create_put_filename()
        s3.upload(TEMPFILE, BUCKET, put_filename)

        return jsonify({"success": True, "filename": put_filename})

    return jsonify({"success": False, "filename": None})


def create_put_filename():
    suffix = ".jpg"
    return "%s/%s%s" % (os.environ["BUCKET_PATH"], str(uuid.uuid4()), suffix)


#      base64 = encodeToBase64(filename)
#      print (base64)
#  print (datetime.datetime.today())
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
