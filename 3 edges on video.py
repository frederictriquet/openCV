import cv2 as cv

capture = cv.VideoCapture(0)

k=None
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
while k != 27:
    isTrue, frame = capture.read()
    canny = cv.Canny(cv.flip(frame, 1), 100, 20, apertureSize=3)

    cv.imshow('test', canny)

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()

