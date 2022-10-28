import cv2 as cv
import numpy as np

img = cv.imread("lenna.png", cv.IMREAD_COLOR)

for channel in range(3):
    temp = np.zeros(img.shape, dtype=np.uint8)
    temp[:,:,channel] = img[:,:,channel]
    cv.imshow("channel_"+str(channel), temp)

cv.waitKey(0)
cv.destroyAllWindows()