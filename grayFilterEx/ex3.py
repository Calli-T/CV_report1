import cv2 as cv
import numpy as np

def mean33(before):
    after = np.copy(origin)
    filter = np.array([[1/9, 1/9, 1/9, 1/9, 1/9], [1/9, 1/9, 1/9, 1/9, 1/9], [1/9, 1/9, 1/9, 1/9, 1/9], [1/9, 1/9, 1/9, 1/9, 1/9], [1/9, 1/9, 1/9, 1/9, 1/9]])

    x, y = before.shape

    for i in range(1, x - 1):
        for j in range(1, y - 1):
            after[i, j] = 0

            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    after[i, j] += filter[k+1, l+1] * before[i+k, j+l]

    return after

def mean55(before):
    after = np.copy(origin)
    filter = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],[0.04, 0.04, 0.04, 0.04, 0.04],[0.04, 0.04, 0.04, 0.04, 0.04],[0.04, 0.04, 0.04, 0.04, 0.04],[0.04, 0.04, 0.04, 0.04, 0.04]])

    x, y = before.shape

    for i in range(2, x - 2):
        for j in range(2, y - 2):
            after[i, j] = 0

            for k in [-2, -1, 0, 1, 2]:
                for l in [-2, -1, 0, 1, 2]:
                    after[i, j] += filter[k+2, l+2] * before[i+k, j+l]

    return after


origin=cv.imread("Lenna.png", cv.IMREAD_GRAYSCALE)
filtered_mean33=mean33(origin)
filtered_mean55=mean55(origin)

cv.imshow('Origin', origin)
cv.imshow('Mean_33', filtered_mean33)
cv.imshow('Mean_55', filtered_mean55)


cv.waitKey(0)
cv.destroyAllWindows()