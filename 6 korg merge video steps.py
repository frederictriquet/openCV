import cv2 as cv
import mido

capture = cv.VideoCapture(0)
port = mido.open_input('nanoKONTROL2 SLIDER/KNOB')
values = [ 0, 0 ]
kontrols = [ 0, 1 ]

k=None
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
while k != 27:
    isTrue, frame = capture.read()
    for msg in port.iter_pending():
        if msg.control in kontrols:
            index = kontrols.index(msg.control)
            values[index] = msg.value
    alpha = 1.0*values[0]/127.0
    beta = 1.0 - alpha

    merged = cv.addWeighted(frame, alpha, previous, beta, 0.)
    cv.imshow('test', merged)

    previous = merged

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()

