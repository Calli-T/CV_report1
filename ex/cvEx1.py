import cv2
img=cv2.imread("Lenna.png")
print(img.shape)

cv2.imshow('image1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img[164][164])

