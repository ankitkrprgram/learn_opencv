import cv2
img = cv2.imread("banner.jpg")
cv2.imshow("banner", img)

blur_img = cv2.GaussianBlur(img, (15, 15), 10)
cv2.imshow("blur_img", blur_img)

cv2.waitKey(0)
