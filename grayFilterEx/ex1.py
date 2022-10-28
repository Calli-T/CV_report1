import cv2 as cv
import numpy as np

def meanFilter(before):
    after = np.copy(origin)

    x, y = before.shape
    print(x, y)

    for i in range(1, x - 1):
        for j in range(1, y - 1):
            after[i, j] = before[i-1, j-1]*(1/9) + before[i-1, j]*(1/9) + before[i-1, j+1]*(1/9) + before[i, j-1]*(1/9) + before[i, j]*(1/9) + before[i, j+1]*(1/9) + before[i+1, j-1]*(1/9) + before[i+1, j]*(1/9) + before[i+1, j+1]*(1/9)

    return after

origin=cv.imread("Lenna.png", cv.IMREAD_GRAYSCALE)
filtered1=meanFilter(origin)

cv.imshow('Origin', origin)
cv.imshow('Mean', filtered1)


cv.waitKey(0)
cv.destroyAllWindows()