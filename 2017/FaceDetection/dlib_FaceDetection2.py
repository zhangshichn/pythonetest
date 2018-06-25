#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import sys
import numpy as np
import dlib
import cv2


#面部區域檢測輸出,矩陣區域的邊界
def rect_to_bb(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return (x, y, w, h)


#將shape函數輸出的68個面部識別點,轉換成numpy array
def shape_to_np(shape, dtype="int"):
    coords = np.zeros((68,2),dtype=dtype)
    for i in range(0,68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords

#修改輸入圖片的尺寸,避免過大
def resize(image, width=1200):
    r = width * 1.0 / image.shape[1]
    dim = (width, int(image.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized

if len(sys.argv) < 2:
    print("Usage: %s <image file>" %sys.argv[0])
    sys.exit(1)

#從sys.argv[1]中讀取圖片,初始化面部區域檢測detector和面部特徵識別predictor
image_file = sys.argv[1]
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")


#opencv加載圖片,resize到適合的大小,轉成灰度圖,detector檢測面部區域,返回多張面部信息數組rects
image = cv2.imread(image_file)
image = resize(image, width=1200)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rects = detector(gray, 1)


#對每張面部做進一步特徵檢測,臉部區域用綠框顯示,臉部特徵用紅點顯示,cv2.waitKey(0)是任意鍵退出
for (i, rect) in enumerate(rects):
    shape = predictor(gray, rect)
    shape = shape_to_np(shape)

    (x, y, w, h) = rect_to_bb(rect)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    for (x, y) in shape:
        cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

cv2.imshow("Output", image)
cv2.waitKey(0)