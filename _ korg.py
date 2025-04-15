import cv2 as cv
import mido
from math import cos, sin
import numpy as np

capture = cv.VideoCapture(0)
port = mido.open_input('nanoKONTROL2 SLIDER/KNOB')
k=None
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, previous = capture.read()
values = [25, 11, 67, 127, 50, 33, 20]
kontrols = [ 0, 1, 2, 3, 4, 5, 6 ]
print(previous.shape)
rows,cols, _ = previous.shape
t = 0
ax = 0
ay = 0
at = 0
while k != 27:
    isTrue, frame = capture.read()
    updated = False
    for msg in port.iter_pending():
        if msg.control in kontrols:
            updated = True
            index = kontrols.index(msg.control)
            values[index] = msg.value
    if updated:
        print(values)

    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,apertureSize = 3)
    lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv.line(frame,(x1,y1),(x2,y2),(0,255,0),2)

    cv.imshow('test', frame)

    previous = frame

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()

