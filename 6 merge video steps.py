import cv2 as cv

capture = cv.VideoCapture(0)

k=None
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
_, previous = capture.read()
while k != 27:
    isTrue, frame = capture.read()

    alpha = 0.1
    beta = 1.0 - alpha

    merged = cv.addWeighted(frame, alpha, previous, beta, 0.)
    cv.imshow('test', merged)

    previous = merged

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()

