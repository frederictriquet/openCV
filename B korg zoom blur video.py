import cv2 as cv
import mido
from math import cos, sin

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

    # center = (
    #     (cols-1)/2.0 +values[5]*(values[3]-64),
    #     (rows-1)/2.0 +values[5]*(values[4]-64)
    # )

    time_speed, raw_alpha, zoom, r, sx, sy, tilt_speed = values
    t += 0.01*time_speed

    ax += 0.01*time_speed*sx/64.0
    ay += 0.01*time_speed*sy/64.0
    center = (
        (cols-1)/2.0 + r*cos(ax),
        (rows-1)/2.0 + r*sin(ay)
    )
    at += 0.01*tilt_speed
    tilt = 4.0*sin(at)
    M = cv.getRotationMatrix2D(center=center, angle=tilt, scale=(zoom+1)/64.0)

    alpha = 1.0*raw_alpha/127.0
    beta = 1.0 - alpha

    merged = cv.addWeighted(frame, alpha, previous, beta, 0.)
    rotated = cv.warpAffine(merged, M, (cols,rows))
    cv.imshow('test', rotated)

    previous = rotated

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()

