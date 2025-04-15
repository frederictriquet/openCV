import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)# + cv.CAP_DSHOW)


WIDTH, HEIGHT = 800, 600
capture.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)
font = cv.FONT_HERSHEY_SIMPLEX
cell_width, cell_height = 12, 12
new_width, new_height = int(WIDTH / cell_width), int(HEIGHT / cell_height)

k=None
isTrue, previous = capture.read()
isTrue, previous = capture.read()
isTrue, previous = capture.read()
isTrue, previous = capture.read()

while k != 27:
    isTrue, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    inverted = 255 - gray
    k = 31
    blurred = cv.GaussianBlur(inverted, (k, k), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv.divide(gray, inverted_blurred, scale=256.0)

    cv.imshow('test', pencil_sketch)

    # previous = frame

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()
