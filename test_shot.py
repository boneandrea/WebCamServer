# -*- coding: utf-8

import sys
import cv2

c = cv2.VideoCapture(0)

# サイズを指定しないと"select timeout"した
c.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1200)
c.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 800)

print c
if not c.isOpened():
  print ("cam is not open");
  sys.exit(1)


print "start to capture"
r, img = c.read()
print "shot"


if r:
  # 保存
  cv2.imwrite("img/abc.jpg", img)
  ret=0
else:
  print "fail"
  ret=1

c.release()
sys.exit(ret)

#      base64 = encodeToBase64(filename)
#      print (base64)
#  print (datetime.datetime.today())

