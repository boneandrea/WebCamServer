# -*- coding: utf-8

from flask import Flask, request, render_template
import cv2


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
        cv2.imwrite("img/abc.jpg", img)
        code = 200
        message = ""
    else:
        message = "fail"
        code = 503

    c.release()
    return render_template('index.html', message=message), code


#      base64 = encodeToBase64(filename)
#      print (base64)
#  print (datetime.datetime.today())
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
