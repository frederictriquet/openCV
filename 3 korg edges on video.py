import cv2 as cv
import mido

capture = cv.VideoCapture(0)
port = mido.open_input('nanoKONTROL2 SLIDER/KNOB')
k=None
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
values = [ 0, 0, 0, 0 ]
kontrols = [ 0, 1, 2, 3 ]
while k != 27:
    isTrue, frame = capture.read()
    for msg in port.iter_pending():
        if msg.control in kontrols:
            index = kontrols.index(msg.control)
            values[index] = msg.value
    canny = cv.Canny(cv.flip(frame, 1), values[0], values[1], apertureSize=3)

    cv.imshow('test', canny)

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()

