import cv2 as cv

capture = cv.VideoCapture(0)

k=None
while k != 27:
    isTrue, frame = capture.read()
    cv.rectangle(frame, (50,50), (frame.shape[1]//2,frame.shape[0]//2), (255,0,0), thickness=cv.FILLED)
    cv.circle(frame, (frame.shape[1]//4*3, frame.shape[0]//4*3), 40, (0,0,255), thickness=-1)

    cv.imshow('test', frame)
    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()

