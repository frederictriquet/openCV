import cv2 as cv

capture = cv.VideoCapture(0)

k=None
isTrue, previous = capture.read()
while k != 27:
    isTrue, frame = capture.read()

    bitwise = cv.bitwise_xor(frame, previous)

    cv.imshow('test', bitwise)

    previous = frame

    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()

