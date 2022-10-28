import cv2 as cv
img1=cv.imread("Lenna.png", cv.IMREAD_GRAYSCALE)


x,y=img1.shape
print(x,y)

for i in range(x):
    for j in range(y):
        img1[i, j] /= 2

cv.imshow('image1', img1)


cv.waitKey(0)
cv.destroyAllWindows()