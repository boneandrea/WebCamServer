# -*- coding: utf-8

import sys
import flask
import base64
import cv2
import time
import tempfile
import datetime

c = cv2.VideoCapture(0)

# サイズを指定しないと"select timeout"した
c.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1200)
c.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 800)

print c

print "start to capture"
r, img = c.read()
print "shot"


if r:
    # 保存
  cv2.imwrite("abc.jpg", img)
  c.release()
  sys.exit(0)
else:
  print "fail"
  c.release()
  sys.exit(1)

#      base64 = encodeToBase64(filename)
#      print (base64)
#  print (datetime.datetime.today())

