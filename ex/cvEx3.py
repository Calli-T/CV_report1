import cv2
img1 = cv2.imread("Lenna.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("Lenna.png")

print(img1.shape)
print(img2.shape)

print(img1[165][165])
print(img2[165][165])

for i in range(330):
    print((img2[i,i,0]+img2[i,i,1]+img2[i,i,2]))
    print(img1[i][i])