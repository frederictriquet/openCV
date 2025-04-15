import cv2 as cv

capture = cv.VideoCapture(0)
isTrue, frame = capture.read()

img = cv.imread('abeille.jpeg')
print(img.shape)
img = cv.resize(img, (frame.shape[1],frame.shape[0]))
print(img.shape)
k=None
while k != 27:
    isTrue, frame = capture.read()
    print(img.shape, frame.shape)
    blended = cv.addWeighted(img, 0.5, frame, 0.5, 0.0)

    cv.imshow('test', blended)
    k = cv.waitKey(20)

capture.release()
cv.destroyAllWindows()


