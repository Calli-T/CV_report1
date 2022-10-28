import cv2 as cv
import numpy as np


def mean33(before):
    after = np.copy(origin)
    filter = np.array(
        [[1 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9],
         [1 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9]])

    x, y = before.shape

    for i in range(1, x - 1):
        for j in range(1, y - 1):
            after[i, j] = 0

            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    after[i, j] += filter[k + 1, l + 1] * before[i + k, j + l]

    return after


def mean55(before):
    after = np.copy(origin)
    filter = np.array([[0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04],
                       [0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04]])

    x, y = before.shape

    for i in range(2, x - 2):
        for j in range(2, y - 2):
            after[i, j] = 0

            for k in [-2, -1, 0, 1, 2]:
                for l in [-2, -1, 0, 1, 2]:
                    after[i, j] += filter[k + 2, l + 2] * before[i + k, j + l]

    return after


def median33(before):
    after = np.copy(origin)
    filter = np.zeros([3, 3])

    x, y = before.shape

    for i in range(1, x - 1):
        for j in range(1, y - 1):
            slice = np.sort(np.array(before[i - 1:i + 2, j - 1:j + 2]).reshape(1, -1))
            after[i, j] = slice[0][4]

    return after

def median55(before):
    after = np.copy(origin)
    filter = np.zeros([5, 5])

    x, y = before.shape

    for i in range(2, x - 2):
        for j in range(2, y - 2):
            slice = np.sort(np.array(before[i - 2:i + 3, j - 2:j + 3]).reshape(1, -1))
            after[i, j] = slice[0][12]

    return after


origin = cv.imread("Lenna.png", cv.IMREAD_GRAYSCALE)
filtered_mean33=mean33(origin)
filtered_mean55=mean55(origin)
filtered_median33 = median33(origin)
filtered_median55 = median55(origin)

cv.imshow('Origin', origin)
cv.imshow('Mean_33', filtered_mean33)
cv.imshow('Mean_55', filtered_mean55)
cv.imshow('Median_33', filtered_median33)
cv.imshow('Median_55', filtered_median55)

cv.waitKey(0)
cv.destroyAllWindows()
