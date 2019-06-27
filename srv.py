# -*- coding: utf-8

from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import cv2
import time
import uuid
import os
import s3


load_dotenv()
width = float(os.environ["IMAGE_WIDTH"])
height = float(os.environ["IMAGE_HEIGHT"])
CAMERA_RELEASE_WAIT = int(os.environ["CAMERA_RELEASE_WAIT"])

TEMPFILE = "img/abc.jpg"
BUCKET = os.environ["BUCKET"]


def init_cam():
    c = cv2.VideoCapture(0)
# サイズを指定しないと"select timeout"した
    c.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, width)
    c.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, height)
    print(c)
    return c


app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html', title='Home')


@app.route('/shot')
def my_shot():
    c = init_cam()
    if not c.isOpened():
        print("cam is not open")
        return render_template('index.html', message="cam is not open"), 503

    print("start to capture")
    r, img = c.read()
    print("shot")

    if r:
       # 保存
        cv2.imwrite(TEMPFILE, img)

        put_filename = create_put_filename()
        s3.upload(TEMPFILE, BUCKET, put_filename)

        success = True
    else:
        put_filename = None
        success = False

    release_camera(c)
    return jsonify({"success": success, "filename": put_filename})


def release_camera(c):
    c.release()
    time.sleep(CAMERA_RELEASE_WAIT)


def create_put_filename():
    suffix = ".jpg"
    return "%s/%s%s" % (os.environ["BUCKET_PATH"], str(uuid.uuid4()), suffix)


#      base64 = encodeToBase64(filename)
#      print (base64)
#  print (datetime.datetime.today())
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
