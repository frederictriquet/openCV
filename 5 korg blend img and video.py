import cv2 as cv
import mido
port = mido.open_input('nanoKONTROL2 SLIDER/KNOB')
values = [ 0, 0 ]
kontrols = [ 0, 1 ]

capture = cv.VideoCapture(0)
isTrue, frame = capture.read()

img = cv.imread('abeille.jpeg')
print(img.shape)
img = cv.resize(img, (frame.shape[1],frame.shape[0]))
print(img.shape)
k=None
while k != 27:
    isTrue, frame = capture.read()
    for msg in port.iter_pending():
        if msg.control in kontrols:
            index = kontrols.index(msg.control)
            values[index] = msg.value
    alpha = 1.0*values[0]/127.0
    beta = 1.0 - alpha

    blended = cv.addWeighted(img, alpha, frame, beta, 0.0)

    cv.imshow('test', blended)
    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()


