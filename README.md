# What

pythonでCV2を用いて写真を撮る
2か3かどうするか

# How

## デバイスは指すだけで認識する

```
lsusb
ls /dev/video*
```

## Python3

```
sudo apt install libcblas3 libatlas3-base libjasper1 libqt4-test libqtgui4
pip3 install opencv-python # 見つからない
```
しかしnumpyがエラーを吐いて動かない  
解決はすげえ手間がかかるらしい。全部コンパイル？
virtualenvでpipでポイポイとは行かない。

```
python3
>> import cv2
numpy failed
```

## Python2

`pip install opencv-python` は同様に見つからない
apt で*.so持ってくるしかない
```
sudo apt-get install libopencv-dev
python test_shot.py
```
動いた
