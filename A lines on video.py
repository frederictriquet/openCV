import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
k=None
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, frame = capture.read()
isTrue, previous = capture.read()

while k != 27:
    isTrue, frame = capture.read()

    img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    img = cv.medianBlur(img,5)
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,10,20*5,
                                param1=50,param2=30,minRadius=0,maxRadius=200)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv.circle(frame,(i[0],i[1]),2,(0,0,255),3)

    # gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # edges = cv.Canny(gray,50,150,apertureSize = 3)
    # lines = cv.HoughLinesP(edges,1,np.pi/180,10,minLineLength=5,maxLineGap=20)

    # blur = cv.medianBlur(frame,5)
    # circles = cv.HoughCircles(blur,cv.HOUGH_GRADIENT,1,20,
    #                             param1=50,param2=30,minRadius=0,maxRadius=0)
    # circles = np.uint16(np.around(circles))
    # for i in circles[0,:]:
    #     # draw the outer circle
    #     cv.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
    #     # draw the center of the circle
    #     cv.circle(frame,(i[0],i[1]),2,(0,0,255),3)


    # for line in lines:
    #     x1,y1,x2,y2 = line[0]
    #     cv.line(frame,(x1,y1),(x2,y2),(0,255,0),2)

    cv.imshow('test', frame)

    previous = frame
    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()

