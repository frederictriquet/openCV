import cv2 as cv

capture = cv.VideoCapture(0)

k=None
previous = None
while k != 27:
    isTrue, frame = capture.read()

    if previous is not None:
        bitwise = cv.absdiff(frame, previous)

        cv.imshow('test', bitwise)

    previous = frame

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()
