import cv2 as cv

x1=300
x2=700
dx=200

y1=100
y2=500
dy=200
img = cv.imread('abeille.jpeg')
r = img[y1:y1+dy , x1:x1+dx]
img[y2:y2+dy, x2:x2+dx] = r
cv.imshow('test', img)
cv.waitKey(0)
cv.destroyAllWindows()

