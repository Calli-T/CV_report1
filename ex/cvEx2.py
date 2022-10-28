import cv2
img1=cv2.imread("Lenna.png")
img2=cv2.imread("Lenna.png", cv2.IMREAD_REDUCED_COLOR_2)
img3=cv2.imread("Lenna.png", cv2.IMREAD_REDUCED_COLOR_4)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('image3', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()