from math import cos, sin
import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)# + cv.CAP_DSHOW)


cell_width, cell_height = 40,30
k=None
isTrue, previous = capture.read()
isTrue, previous = capture.read()
isTrue, previous = capture.read()
isTrue, previous = capture.read()

width = previous.shape[1]
height = previous.shape[0]
print(width, height)
nb_width, nb_height = int(width / cell_width), int(height / cell_height)
print(nb_width, nb_height)

t = 0
dx = cell_width
dy = cell_height
while k != 27:
    isTrue, frame = capture.read()
    t += 1
    frame2 = frame.copy()
    # black_window = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    for i in range(1,nb_width-1):
        for j in range(1,nb_height-1):

            x1 = i*cell_width
            y1 = j*cell_height
            x2 = x1 #+ int(cell_width*cos((t+i)*0.19))
            y2 = y1 + int(cell_height*sin((t+i)*0.16))
            # cv.circle(black_window, coord, 5, (B, G, R), 2)
            # r = (i*j+t)%5
            r = frame[y1:y1+dy , x1:x1+dx]

            frame2[y2:y2+dy, x2:x2+dx] = r


    cv.imshow('test', frame2)

    previous = frame

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()
