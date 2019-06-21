# -*- coding: utf-8

import flask
import cv2

from flask import Flask, request

def init_cam():
  c = cv2.VideoCapture(0)
# サイズを指定しないと"select timeout"した
  c.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1200)
  c.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 800)
  print(c)
  return c

app = Flask(__name__)
@app.route('/')
def hello_world():
  return "Hello World!"

@app.route('/shot')
def my_shot():
  c=init_cam()
  if not c.isOpened():
    print ("cam is not open");
    return "Camera initialization failed"

  print ("start to capture")
  r, img = c.read()
  print ("shot")

  if r:
     # 保存
    cv2.imwrite("abc.jpg", img)
  else:
    print ("fail")

  c.release()
  return "Hello World!"

#      base64 = encodeToBase64(filename)
#      print (base64)
#  print (datetime.datetime.today())
if __name__ == '__main__':
  app.run(host="0.0.0.0",debug=True)


