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

    img = cv.detailEnhance(frame)
    # img = cv.edgePreservingFilter(frame)
    # img1, img = cv.pencilSketch(frame)
    # img = cv.stylization(frame)

    cv.imshow('test', img)

    previous = frame

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()
