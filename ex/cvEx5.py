import cv2 as cv
img1=cv.imread("Lenna.png")

cv.imshow('image1', img1)

x,y,bgr=img1.shape
print(x,y,bgr)

cv.waitKey(0)
cv.destroyAllWindows()